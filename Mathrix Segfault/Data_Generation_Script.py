import Pandemic_Model as pm
import ProbabilityWRTAge as pwrtage
import csv
import blood_pressure as bp
import math
import random
import numpy as np

#Dhanush Srikanth
def death_val(x):
    return (0.05*(math.tanh((x - 67)/27)) + 0.05 + (0.0003*(50 - x)))
                 
#Respiratory Data provided by Krishna Singh
resp = [0.0021582959853330393, 0.002304820563869844, 0.0024310782597921693, 0.002538174641583738, 0.0026271958264305457, 0.0026992084802208577,
               0.0027552598175452133, 0.0027963776016964245, 0.0028235701446695733, 0.002837826307162016, 0.0028401154985733795, 0.002831387677005564,
               0.002812573349262741, 0.0027845835708513547, 0.0027483099459801206, 0.0027046246275600283, 0.002654380317204337, 0.00259841026522858,
               0.002537528270650562, 0.0024725286811903596, 0.002404186393270322, 0.0023332568520150697, 0.002260476051251497, 0.002186560533508769,
               0.0021122073900183237, 0.0020380942607138705, 0.0019648793342313914, 0.0018932013479091396, 0.0018236795877876436, 0.0017569138886097005,
               0.00169348463382038, 0.0016339527555670264, 0.001578859734699252, 0.0015287276007689462, 0.001484058932030268, 0.001445336855439648,
               0.0014130250466557904, 0.0013875677300396677, 0.0013693896786545335, 0.0013588962142659004, 0.0013564732073415688, 0.0013624870770515935,
               0.0013772847912683175, 0.0014011938665663482, 0.0014345223682225674, 0.0014775589102161235, 0.0015305726552284427, 0.0015938133146432274,
               0.0016675111485464419, 0.0017518769657263273, 0.0018471021236733988, 0.0019533585285804365, 0.0020707986353425117, 0.0021995554475569452,
               0.0023397425175233325, 0.002491453946243561, 0.002654764383421771, 0.0028297290274643797, 0.00301638362548008, 0.0032147444732798336,
               0.0034248084153768797, 0.003646552844986724, 0.003879935704027149, 0.004124895483118183, 0.004381351221582179, 0.004649202507443718,
               0.004928329477429682, 0.0052185928169691895, 0.005519833760193672, 0.005831874089936793, 0.006154516137734535, 0.0064875427838251,
               0.006830717457149025, 0.007183784135349041, 0.0075464673447702135, 0.007918472160459863, 0.008299484206167584, 0.008689169654345215,
               0.009087175226146908, 0.00949312819142907, 0.009906636368750374, 0.01032728812537175, 0.010754652377256453, 0.011188278589069964,
               0.01162769677418005, 0.012072417494656767, 0.012521931861272382, 0.012975711533501513, 0.013433208719521018, 0.013893856176210001,
               0.014357067209149893, 0.014822235672624338, 0.015288735969619265, 0.015755923051822933, 0.016223132419625808, 0.01668968012212068,
               0.01715486275710252, 0.01761795747106866, 0.018078221959218727, 0.018534894465454484, 0.018987193782380115, 0.019434319251301988,
               0.01987545076222876, 0.02030974875387139, 0.020736354213643116, 0.021154388677659345, 0.021562954230737882, 0.021961133506398743,
               0.022347989686864182, 0.02272256650305884, 0.023083888234609537, 0.023430959709845402, 0.023762766305797763, 0.0240782739482003,
               0.02437642911148903, 0.02465615881880204, 0.02491637064197986, 0.025155952701565235, 0.025373773666803157, 0.025568682755640972, 0.025739509734728203]
diabetes = []
#Pragadeeshwar Kannan's Diabetes Dataset 
diab = open('DiabDSv2 - DDS.csv', 'r')
reader = csv.reader(diab)
for line in reader:
    diabetes += [line]
for i in range(len(diabetes)):
    diabetes[i][0] = int(diabetes[i][0])-1
for i in range(85, 92):
    diabetes += [[i, float(diabetes[84][1])+random.random()*0.05]]

fields = ['Time of Infection', 'Time of reporting', 'x location', 'y location', 'Age', 'Diabetes', 'Respiratory Illnesses', 'Blood Pressure', 'Outcome']
popfields = ['x location', 'y location', 'Population']

def casebool(p):
    if random.random() <= p:
        return True
    else:
        return False
    
def deathbool(b):
    if random.random() <= b:
        return "Dead"
    else:
        return "Alive"

mup = 28+random.random()*14
l = np.zeros(91)
l = pwrtage.probabilityByAge(mup)*10**4
agetrials = []
for i in range(len(l)):
    for k in range(int(l[i])):
	    agetrials += [i]
    
datafile = open('COVID_Dataset.csv', 'w')
popfile = open('Population.csv', 'w')
writer = csv.writer(datafile)
popwriter = csv.writer(popfile)
writer.writerow(fields)
popwriter.writerow(popfields)           #LMAO this doesn't actually work (can't open multiple writer objects at once?) so Population.csv had to be written from shell.
print("Population of City", pm.net_pop(239))
print("Cumulative Infection Count at End", pm.net_cases(239))
print("mup", mup)

for t in range(240):
    for i in range(1, 21):
        for j in range(1, 21):
            for k in range(int(pm.cases[i][j][t])):
                age = agetrials[random.randint(0,len(agetrials)-1)]
                entry = [t, t + random.randint(1, 7), i, j,age,casebool(float(diabetes[age][1])),casebool(resp[age]/pwrtage.probabilityByAge(mup)[age]),
                             casebool(bp.bloodpressure(age)), deathbool(death_val(age))]
                writer.writerow(entry)

#LMAO this doesn't actually work (can't open multiple writer objects at once?) so Population.csv had to be written from shell.
for i in range(1,21):
    for j in range(1,21):
        popwriter.writerow([i, j, pm.tot_pop[i][j][239]])
    
        
                



    





