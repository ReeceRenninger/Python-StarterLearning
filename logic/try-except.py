#try / except allows the program to continue running even if there is an error
def div42by(divideBy):
    try:
        return 42 / divideBy
    # this error is raised when you try to divide by zero
    # specific error that was presented in terminal
    except ZeroDivisionError:
        print('Error: You tried to divide by zero.')

print(div42by(2))
print(div42by(12))
print(div42by(0))
print(div42by(1))

# this is a way to handle errors in a program
print('How many cats do you have?')
numCats = input()
try:
    if int(numCats) >= 4:
      print('That is a lot of cats.')
    elif int(numCats) >= 0:
      print('That is not that many cats.')
    else:
       # this is a way to raise an error for negative numbers specifically here
       raise ValueError
except ValueError:
    print('You did not enter a valid number.')
