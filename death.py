import math
import random

def death_val(x):
  if x > 5:
  
    return (0.05*(math.tanh((x - (67 - random.random()*20)/27 - random.random()*10)) + 0.05 + (0.00002*(50 - random.random()*10 - x))
    
