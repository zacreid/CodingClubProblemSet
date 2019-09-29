'''
     Coding Club Quick Test Prime Three - Zac Reid

 - How it works?
 
 - Given an input of a list of numbers find all the numbers that meet the following criteria
     - A prime number
     - Contains the number 3

 - All numbers found that meet this criteria must be then sorted by how many times the number three occurs
  (numbers with the same number of threes should be sorted according to there numerical value) 
 
 - Example input [2, 3, 10, 55, 37, 323, 533, 333, 22, 103, 57]
 - Example output [3, 37, 103]
 (1 <= len(input) <= 100)
 (1 <= input <= 1000)
 '''

def primethree(inp):
    x = lambda a : str(a).count('3')

    for i in inp[:]:
        if x(i) == 0:
            inp.remove(i)
            continue

        for y in range(2, (i//2) + 2):
            if i % y == 0:
                inp.remove(i)
                break
    
    return sorted(inp, key=x)


inp = list(range(1,1000))
print(primethree(inp))