# Sort the words alphabetically entered by user
from os import system

def say(var):
    system( 'say "%s"' % var)

# take input from the user

say ("Enter a string")
input_str = input("Enter a string: ")

# split the string into a list of words
words = input_str.split()
words
# sort the list in order
words.sort()

# print the sorted words
for word in words:
   print(word)
   say(word)
