# Write a random number generator that generates random numbers between 1 and 6 
# (simulates a dice)
import random

def roll():
    #1
    #return int(random.random() *6 )+ 1
    
    #2
    #return random.randrange(1,6,1)
    
    #3
    return random.randint(1,6)
    

print(roll())