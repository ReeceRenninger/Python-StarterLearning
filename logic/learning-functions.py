#standard library
import math
import sys
# two ways to import from random, import module is usually better
import random
# from random import *

## 3rd party modules

# returns a random number between 1 and 10
def random_number():
  return random.randint(1, 10)

# there is also sys.exit() to exit the program
print("Random number: ", random_number())
# sys.exit()
# the system greys this out because the sys.exit() prevents it from running
# print("This will not print")

#!! functions
# hello function is fed an argument of name so when it is called it MUST receive a parameter
def hello(name):
  print('hey there ' + name)


# calls the hello function and prints the messages
hello('Alice')
hello('Ryan')

# end='' prevents the print function from creating a new line
print('Hello', end='')
print('World')

# sep='' changes the default separator from a space to , so the print function will print the values with a comma and a space
print('cats', 'dogs', 'mice', sep=', ')

# function with simple math logic that can be used within a variable to call the function to generate the variable new value

def plusOne(number):
  return number + 1

newNumber = plusOne(5)
print(newNumber)
