import numpy as np
import matplotlib.pyplot as plt

#City Size (gridx and gridy initialized here are +2 more than the actual city size)
gridx = 22
gridy = 22

#Total time of simulation
T = 240

# degrees of influence
ind = 8

#Initializing relevant matrices
cases = np.zeros((gridx, gridy, T))
tot_cases  = np.zeros((gridx, gridy, T))

#tot_pop for convenience is generate using the same diffusion; this has no real meaning though
tot_pop = np.zeros((gridx, gridy, T))

p = np.zeros((ind, gridx, gridy, T))      
diff = np.zeros((gridx, gridy, T))

#Transmission rate and diffusion coefficient(s) (Case diff_c < diff_c)
trans_rate = 1.01
case_diff_c = 0.25
diff_c = 0.9
fall = 0.03

#Points of index cases and population diffusion start
no_src = 40
sources = np.random.rand(2,no_src)
sources[0] = sources[0]*gridx
sources[1] = sources[1]*gridy
common_start = 100

#IT IS ESSENTIAL FOR POPULATION AND CASES TO HAVE THE SAME INITIAL CONDITIONS!!!
#Index case(s)
for i in range(no_src):
    cases[int(sources[0][i])][int(sources[1][i])][0] = common_start
    tot_cases[int(sources[0][i])][int(sources[1][i])][0] = cases[int(sources[0][i])][int(sources[1][i])][0]


#Initial condition(s) for tot_pop diffusion
pop_fall = 0.1
for i in range(no_src):
    tot_pop[int(sources[0][i])][int(sources[1][i])][0] = common_start

#Initializing amount of diffusion for cases (Anisotropic)
for i in range(gridx):
    for j in range(gridy):
        diff[i][j][0] = 0.001*np.random.randint(400, 1000)*case_diff_c
        s = diff[i][j][0]
        for k in range(ind - 1):
            #Highly Anistropic Diffusion
            p[k][i][j][0] = np.random.random()*s
            s -= p[k][i][j][0]
            
            #For isotropy
            #p[k][i][j][0] = diff[i][j][0]/8
        #p[ind-1] = diff[i][j][0]/8
            
        p[ind-1] = s
        
#Exponential Decrease in amount of diffusion with time
for i in range(gridx):
    for j in range(gridy):
        for t in range(1, T):
            diff[i][j][t] = diff[i][j][t-1]*np.exp(-fall)
            for k in range(ind):
                p[k][i][j][t] = p[k][i][j][t-1]*np.exp(-fall)
                
#Assigns population on grid using isotropic diffusion; as mentioned before, the diffusion is a matter of convenience, not of any physical meaning
for t in range(1, T):
    for i in range(1, gridx-1):
        for j in range(1, gridy-1):
            tot_pop[i][j][t] = tot_pop[i][j][t-1] + int(np.exp(-pop_fall*t)*0.125*(tot_pop[i+1][j+1][t-1]*diff_c + tot_pop[i][j+1][t-1]*diff_c +
                                         tot_pop[i-1][j+1][t-1]*diff_c + tot_pop[i-1][j][t-1]*diff_c +
                                         tot_pop[i-1][j-1][t-1]*diff_c + tot_pop[i][j-1][t-1]*diff_c +
                                         tot_pop[i+1][j-1][t-1]*diff_c + tot_pop[i+1][j][t-1]*diff_c))

#Cases diffusion; highly anistropic and controlled by population
for t in range(1, T):
    for i in range(1, gridx-1):
        for j in range(1, gridy-1):
            cases[i][j][t] = trans_rate*(tot_cases[i+1][j+1][t-1]*p[4][i+1][j+1][t-1] + tot_cases[i][j+1][t-1]*p[5][i][j+1][t-1] +
                                         tot_cases[i-1][j+1][t-1]*p[6][i-1][j+1][t-1] + tot_cases[i-1][j][t-1]*p[7][i-1][j][t-1] +
                                         tot_cases[i-1][j-1][t-1]*p[0][i-1][j-1][t-1] + tot_cases[i][j-1][t-1]*p[1][i][j-1][t-1] +
                                         tot_cases[i+1][j-1][t-1]*p[2][i+1][j-1][t-1] + tot_cases[i+1][j][t-1]*p[3][i+1][j][t-1])
            
            #Prevents no of cases from exceeding population in area
            if tot_cases[i][j][t-1] + int(cases[i][j][t]) < tot_pop[i][j][T-1]:
                tot_cases[i][j][t] = tot_cases[i][j][t-1] + int(cases[i][j][t])
            else:
                tot_cases[i][j][t] = tot_cases[i][j][t-1]


def plot_tot_cases(t):
    ar = np.zeros((gridx,gridy))
    for i in range(gridx):
        for j in range(gridy):
            ar[i][j] = tot_cases[i][j][t]
    plt.contourf(np.transpose(ar))
    plt.show()

def plot_tot_pop(t):
    ar = np.zeros((gridx,gridy))
    for i in range(gridx):
        for j in range(gridy):
            ar[i][j] = tot_pop[i][j][t]
    plt.contourf(np.transpose(ar))
    plt.show()

def net_cases(t):
    s = 0
    for i in range(1, gridx):
        for j in range(1, gridy):
            s += tot_cases[i][j][t]
    return s

def tot_cases_view(t):
    for i in range(1, gridx):
        for j in range(1, gridy):
            print(tot_cases[i][j][t], end = " ")
        print()

def tot_pop_view(t):
    for i in range(1, gridx):
        for j in range(1, gridy):
            print(tot_pop[i][j][t], end = " ")
        print()
        
def net_pop(t):
    s = 0
    for i in range(1, gridx):
        for j in range(1, gridy):
            s += tot_pop[i][j][t]
    return s

def daily_cases():
    for t in range(1, T):
            if t%10 == 0:
                    print()
            print(net_cases(t)-net_cases(t-1), end = " ")
	
#These are just debug functions to check that cases <= population everywhere    
def compat(t):
    for i in range(1, gridx):
        for j in range(1, gridy):
            if tot_pop[i][j][T-1] < tot_cases[i][j][t]:
                print(i, j, tot_pop[i][j][T-1], tot_cases[i][j][t])
                return False
    return True
def fullcompat():
    for t in range(1, T):
        if compat(t) == False:
            return compat(t)
    return True
