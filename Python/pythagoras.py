'''
     Coding Club Quick Test Pythagoras Therom - Zac Reid

 - How it works?
 
 - a^2 + b^2 = c^2
 - Given a tuple of 2 values (a, b)
 - Find c and return (a, b, c)
 
 - Example input (3, 4) 
 - Example output (3, 4, 5)
 (1 <= input <= 1000)
 '''
import math

def pyth(inp):
    f = lambda a, b : math.sqrt(a**2 + b**2)
    a,b = inp
    return (a, b, f(a,b))

print(pyth((3,4)))