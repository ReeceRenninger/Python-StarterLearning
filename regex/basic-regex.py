import re

message = 'Call me at 555-555-1011 tomorrow. 555-555-9999 is my office.'

# \d is searching for a digit character
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
#match object
mo = phoneNumRegex.search(message)
# findall() method returns a list of strings wrapped in []
print(phoneNumRegex.findall(message))
print('this is the match object search ' + mo.group())


# non regular expression
def isPhoneNumber(text):
    if len(text) != 12:
        return False # not phone number-sized
    for i in range(0, 3):
        if not text[i].isdecimal(): # no area code
            return False
    if text[3] != '-':
            return False # missing dash
    for i in range(4, 7):
         if not text[i].isdecimal(): # no first 3 digits
            return False
    if text[7] != '-': # missing second dash
            return False
    for i in range(8, 12): # missing last 4 digits
        if not text[i].isdecimal():
            return False
    return True # "text" is a phone number!

message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
foundNumber = False

for i in range(len(message)):
    chunk = message[i:i+12] # slice the string
    if isPhoneNumber(chunk):
        print('Non regex function: Phone number found: ' + chunk)
        foundNumber = True
if not foundNumber:
    print('Could not find any phone numbers.')

# print(isPhoneNumber('415-555-1234'))
# print(isPhoneNumber('hello'))