import math
import random

def death_val(x):
  
   return (0.05*(math.tanh((x - (67 - random.random()*20)/27 - random.random()*10)) + 0.05 + (0.0003*(50 - random.random()*10 - x))
    
