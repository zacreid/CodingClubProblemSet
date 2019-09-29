'''
     Coding Club Quick Test FizzBuzz - Zac Reid

 - How it works?

 - If it is divisable by 3 say Fizz
 - If it is divisable by 5 say Buzz
 - If both of the above statements are true say FizzBuzz
 
 - Example output 1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz
 (1 <= input <= 100)
 '''
def fizzBuzz(num):
    if num % 15 == 0:
        return 'FizzBuzz'

    if num % 3 == 0:
        return 'Fizz'

    if num % 5 == 0:
        return 'Buzz'

    return num
    
for x in range(1000):
    print(fizzBuzz(x))