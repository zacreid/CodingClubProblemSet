'''
     Coding Club Quick Test Palindrome - Zac Reid

 - How it works?
 
 - Given a word (containing higher or lower case letters) if you reversed the word would it stay the same (the word is a palindrome)

 - Example input 'Bob' 'Sally' 'Anna' 'wow'
 - Example output True False True True
 
 - You could improve this example by allowing the input of phrases and sentences! (e.g "Taco Cat" -> True)
 '''

# single words
inp = input(" : ").lower()
print(inp == inp[::-1])

# phrases and sentences
inp = inp.replace(' ', '')
print(inp == inp[::-1])