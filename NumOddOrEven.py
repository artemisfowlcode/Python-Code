from os import system
# program to check if the input number is odd or even.
# if a number devided by 2 gives a remainder of 0 means it's even
# If remainder is 1, it is odd number.

def say(var):
    system( 'say "%s"' % var)

num = int(input("Please enter a number: "))
if (num % 2) == 0:
   say("{0} is Even".format(num))
   print("{0} is Even".format(num))
else:
   say("{0} is Odd".format(num)) 
   print("{0} is Odd".format(num))
