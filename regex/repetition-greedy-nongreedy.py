import re

# the ? character can be used to MATCH ZERO OR ONE of the group preceding it
# if you needed to find ? in a string using this you can escape it with a backslash such as \?
# the (wo) can appear once or not at all in the string
batRegex = re.compile(r'Bat(wo)?man')
mo = batRegex.search('The Adventures of Batman')
print(mo.group()) # returns Batman

mo = batRegex.search('The Adventures of Batwoman')
# mo = batRegex.search('The Adventures of Batwowowowoman') # this will not match since wo can only appear once, this will return a NoneType error
print(mo.group()) # returns Batwoman

phoneRegex = re.compile(r'(\d\d\d-\d\d\d-\d\d\d\d)')
mo = phoneRegex.search('My phone number is 415-555-1234. Call me tomorrow.')
print(mo.group()) # returns 415-555-1234

# this allows for the area code to be optional
phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo = phoneRegex.search('My phone number is 555-1234. Call me tomorrow.')
print(mo.group()) # returns 555-1234

# the * character can be used to MATCH ZERO OR MORE of the group preceding it
# if you needed to find * in a string, you would need to escape it with a backslash such as \*
batRegex = re.compile(r'Bat(wo)*man')
mo = batRegex.search('The Adventures of Batman')
print(mo.group()) # returns Batman
mo = batRegex.search('The Adventures of Batwoman')
print(mo.group()) # returns Batwoman
mo = batRegex.search('The Adventures of Batwowowowoman')
print(mo.group()) # returns Batwowowowoman

# the + character can be used to MATCH ONE OR MORE of the group preceding it
# if you needed to find + in a string, you would need to escape it with a backslash such as \+
batRegex = re.compile(r'Bat(wo)+man')
mo = batRegex.search('The Adventures of Batman')
print(mo) # returns None
mo = batRegex.search('The Adventures of Batwoman')
print(mo.group()) # returns Batwoman
mo = batRegex.search('The Adventures of Batwowowowoman')
print(mo.group()) # returns Batwowowowoman

# the curly braces can be used to MATCH A SPECIFIC NUMBER of the group preceding it
# if you needed to find {3} in a string, you would need to escape it with a backslash such as \{3}
haRegex = re.compile(r'(Ha){3}')
mo = haRegex.search('He said, "HaHaHa"')
print(mo.group()) # returns HaHaHa
# find phone numbers with the certain format
phoneRegex = re.compile(r'((\d\d\d-)?\d\d\d-\d\d\d\d(,)?){3}')
mo = phoneRegex.search('My numbers are 415-555-1234,555-4242,212-555-0000')
print(mo.group()) # returns 415-555-1234,555-4242,212-555-0000

# the curly braces can be used to MATCH A RANGE of the group preceding it
# if you needed to find {3,5} in a string, you would need to escape it with a backslash such as \{3,5}
haRegex = re.compile(r'(Ha){3,5}')
mo = haRegex.search('He said, "HaHaHaHaHa"')
print(mo.group()) # returns HaHaHaHaHa
mo = haRegex.search('He said, "HaHaHa"')
print(mo.group()) # returns HaHaHaHa

# search a range of digits from 3 to 5, as long as 3 digits it will return those 3 up to 5 total digits
digitRegex = re.compile(r'(\d){3,5}')
mo = digitRegex.search('1234567890')
print(mo.group()) # returns 12345

# non greedy matching with the ? after the range will return the shortest string that matches the pattern
digitRegex = re.compile(r'(\d){3,5}?')
mo = digitRegex.search('1234567890')
print(mo.group()) # returns 123

# examples of escaping characters to find
regex = re.compile(r'\+\*\?')
mo = regex.search('I learned about +*? regex syntax')
print(mo.group()) # returns +*?
