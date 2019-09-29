'''
     Coding Club Quick Test SpongeBob - Zac Reid

 - How it works?

 - Get the last digit of any number
 - If it is even say sponge
 - If it is divisable by 3 say bob
 - If both of the above statements are true say spongebob
 - If the number is equal to 9 ignore all the statements above and say patrick
 
 - Example output 10, 11, Sponge, Bob, Sponge, 15, SpongeBob, 17, Sponge, Patrick, 20
 (0 <= input <= 100)
 '''

def spongeBobMod(num):
    '''
     This method uses modulus to get the last number
    '''
    x = num % 10
    if x == 0:
        return num
    if x == 9:
        return 'Patrick'
    if x % 6 == 0:
        return 'SpongeBob'
    if x % 2 == 0:
        return 'Sponge'
    if x % 3 == 0:
        return 'Bob'
    return num
    
def spongeBobString(num):
    '''
     This method uses a string
    '''
    x = int(str(num)[-1])
    string = ''
    if x == 0:
        return num
    if x == 9:
        return 'Patrick'
    if x % 2 == 0:
        string += 'Sponge'
    if x % 3 == 0:
        string += 'Bob'
    if string == '':
        return num
    return string

for x in range(100):
    if not spongeBobMod(x) == spongeBobString(x):
        print("err", x, spongeBobMod(x), spongeBobString(x))