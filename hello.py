# This program says hello and asks for my name

print ('Hello world!')
print ('What is your name?') # ask for their name
myName = input()
print ('It is good to meet you, ' + myName)
print ('The length of your name is:')

# len() function returns the number of characters in a string
print (str(len(myName)) + ' characters long') 

# ask for their age
print ('What is your age?') 

# input() function waits for the user to type some text on the keyboard and press ENTER
myAge = input() 

 # str(), int() functions convert values to strings or integers
print ('You will be ' + str(int(myAge) + 1) + ' in a year.')
