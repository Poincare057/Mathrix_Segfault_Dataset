#Harsh Modani
import random
import math
import numpy as np
muP = 28+(14*(random.random()))
def probabilityByAge (mu) :
    sigma = 25+(10*(random.random()))
    m = 0.0006+(0.0008*(random.random()))
    popByAge, weightForPop, caseByAge= [], [], []
    sum, sumx = 0, 0
    for a in range(90) :
        weightForPop.append(0.001*(150-a))
        popCurr = weightForPop[a]*math.e**(-(((a-muP)/sigma)**2)*0.5)
        popByAge.append(popCurr)
        caseCurr = m*(a+10)
        caseByAge.append(caseCurr)
        sum += popCurr*caseCurr
    case_prop = np.zeros(91)        #Added later; case proportion
    for a in range(90) :
        popByAge[a] /= sum
        #print(a,":",popByAge[a]*caseByAge[a])
        sumx += popByAge[a]*caseByAge[a]
        case_prop[a] = popByAge[a]*caseByAge[a]
        
##    print(muP)
##    print(sigma)
##    print(m)
##    print(sumx)
    return case_prop

#probabilityByAge(muP)
