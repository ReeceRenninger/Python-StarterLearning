# string methods are immutable so they return a new string
spam = 'Hello world!'
spam = spam.upper() # returns 'HELLO WORLD!'
spam = spam.lower() # returns 'hello world!'

answer = input()
if answer.lower() == 'yes': #normalizes the user input to prevent errors
    print('Playing again')

# isupper() and islower() methods return a boolean value
spam = 'Hello world!'
spam.islower() # returns False
spam.isupper() # returns False

# can chain methods together 
spam = 'Hello world!'
spam.upper().lower().upper() # returns 'HELLO WORLD!'

# isaalpha() returns True if the string consists only of letters and is not blank
spam = 'hello'.isalpha() # returns True

# isalnum() returns True if the string consists only of letters and numbers and is not blank
eggs = 'hello123'.isalnum() # returns True

# isdecimal() returns True if the string consists only of numeric characters and is not blank
fries = '123'.isdecimal() # returns True

# isspace() returns True if the string consists only of spaces, tabs, and newlines and is not blank
salad = ' '.isspace() # returns True

# istitle() returns True if the string consists only of words that ALL begin with an uppercase letter followed by only lowercase letters
soup = 'This Is Title Case'.istitle() # returns True
clam = 'this is title case'.title() # returns 'This Is Title Case'

# startswith() and endswith() methods return True if the string value they are called on begins or ends with the string passed to the method
spam = 'Hello world!'
spam.startswith('Hello') # returns True
spam.endswith('world!') # returns True

# join() method is called on a string, gets passed a list of strings, and returns a string
# the returned string is the concatenation of the strings in the list passed to the join() method
# the string joined on is placed between each string in the list
animals = ','.join(['cats', 'rats', 'bats']) 
print(animals) # returns 'cats, rats, bats'

# split() does the opposite of join()
# it's called on a string value and returns a list of strings
# the default split is on whitespace characters
spam = 'My name is Simon'.split()
print(spam) # returns ['My', 'name', 'is', 'Simon']

# ljust() and rjust() methods return a padded version of the string they are called on
# the first argument is an integer length for the returned string
# the second argument is an optional fill character
# if no fill character is specified, a space is used
# ljust() pads the string with the fill character to the left
# rjust() pads the string with the fill character to the right
spam = 'Hello'.rjust(10) # returns '     Hello'
spam = 'Hello'.rjust(20, '*') # returns '***************Hello'
spam = 'Hello'.ljust(10) # returns 'Hello     '
spam = 'Hello'.ljust(20, '*') # returns 'Hello***************'

# center() is similar to ljust() and rjust() but centers the text rather than justifying it to the left or right
spam = 'Hello'.center(20) # returns '       Hello       '
spam = 'Hello'.center(20, '=') # returns '=======Hello========'

# strip() is called on a string and returns a string with whitespace removed from the start and end
# lstrip() and rstrip() remove whitespace from the left and right ends respectively
spam = '    Hello World     '.strip() # returns 'Hello World'
spam = 'SpamSpamBaconSpamEggsSpamSpam'.strip('ampS') # returns 'BaconSpamEggs'

# replace() method is called on a string and returns a new string with all occurrences of the first string replaced by the second string
spam = 'Hello there!'
spam = spam.replace('e', 'XYZ') # returns 'HXYZllo thXYZrXYZ!'
spam = spam.replace('XYZ', 'e') # returns 'Hello there!'

# pyperclip module has copy() and paste() functions that can send text to and receive text from your computer's clipboard

import pyperclip
pyperclip.copy('Hello world!')
pyperclip.paste() # returns 'Hello world!'