# \ is used to escape characters
print('Say hi to Bob\'s mother.')

# different escape characters consist of the following:
# \' single quote
# \" double quote
# \t tab
# \n newline (line break)
# \\ backslash

# new line example
print('Hello there!\nHow are you?\nI\'m doing fine.')

# raw strings are used to ignore escape characters and print the string as is
print(r'That is Carol\'s cat.')

# multiline strings are used to print strings on multiple lines using ''' or """
spam = print('''Dear Alice,
Eve's cat has been arrested for catnapping, cat burglary, and extortion.
Sincerely,
Bob''')

print(spam)

eggs = 'Hello world!'
print(eggs[0]) # prints H
print(eggs[1:5]) # prints from index 1 to 4
print(eggs[-1]) # prints the last character of a string

fries = 'Hello' in 'Hello world!' 
print(fries) # returns True