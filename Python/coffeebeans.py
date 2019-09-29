'''
     Coding Club Quick Test Coffee Beans - Zac Reid

 - How it works?
 
 - Given an input string of any length if the word Coffee or Beans occurs return the word Coffee Beans
 - If above statement is not true return 'sleepy'
 - Must work for capital or lowercase letters
 - Words will be separated with a space (' ')
 
 - Example input "I like coffee", "Beans on toast", "coffee beans", "I only drink tea"
 - Example output 'Coffee Beans', 'Coffee Beans', 'Coffee Beans', 'sleepy'
 (1 <= len(input) <= 1000)
 '''

def coffeeBeans(inp):
    inp = inp.lower().split()

    if 'coffee' in inp or 'beans' in inp:
        return 'Coffee Beans'
    else:
        return 'sleepy'

print(coffeeBeans(input(" : ")))