# Guessing number game

# random module for randint function to generate random number
import random

# print welcome message
print("Welcome to the guessing number game!")
print("What is your name?")
name = input()
print("Well, " + name + ", I am thinking of a number between 1 and 20.")

#create a secret number using random module and randint function built in between 1 and 20
secretNumber = random.randint(1, 20)

# ask player to guess 5 times
# in python for loop, the range function will go up to but NOT include the second argument
# range function will start at 1 and go up to 5
for guessesTaken in range(1, 6):
  print ("Take a guess.")

  # get user input
  guess_input = input()
  # check is user input is a numeric value, this has to be tested on a string BEFORE converting to integer
  # if not does a reverse check, if user input is not a number, print error message and continue to next iteration of for loop
  if not guess_input.isnumeric():
    print(f"{guess_input} is not a number. Please enter a number.")
    continue

  # if user correctly inputted an integer as a string, convert user input to integer
  guess = int(guess_input)

  if guess < secretNumber:
    print("Your guess is too low.")
  elif guess > secretNumber:
    print("Your guess is too high.")
  else:
    break # this condition breaks the for loop with the correct guess

if guess == secretNumber & guessesTaken == 1:
    print(f"Wow, {name}! You guessed my number in 1 guess!")
elif guess == secretNumber:
  print(f"Good job, {name}! You guessed my number in " + str(guessesTaken) + " guesses!")
else:
  print(f"Nope. The number I was thinking of was {secretNumber}.")
