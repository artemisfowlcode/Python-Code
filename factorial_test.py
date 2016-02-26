from os import system
#Example of how to make functions
#Find out the factorial of a given number

#function to print the text
def function_print(line):
    system('say "%s"' % line)

def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n-1)
        
var = "Please enter the number you want to do a factorial for."
print(var)
function_print(var)

number = int(input('?'))
fact = factorial(number)
answer = "The factorial is %d" % fact

print(answer)

function_print(answer)
