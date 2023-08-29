import re

phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# findall() returns a list of strings that match the regex, if there are groups in the regex, it will return a list of tuples
mo = phoneRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(mo) # returns ['415-555-9999', '212-555-0000']

# findall() will not return a Match object, but a list of strings
# if there are no groups in the regex, findall() will return a list of strings
# if there are groups in the regex, findall() will return a list of tuples of strings
phoneRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(mo) # returns [('415', '555-9999'), ('212', '555-0000')]

# character classes can be used to match a set of characters
# \d is a character class that matches any numeric digit from 0 to 9
# \D is a character class that matches any character that is not a numeric digit from 0 to 9
# \w is a character class that matches any letter, numeric digit, or the underscore character
# \W is a character class that matches any character that is not a letter, numeric digit, or the underscore character
# \s is a character class that matches any space, tab, or newline character
# \S is a character class that matches any character that is not a space, tab, or newline character
# the uppercase character classes are the opposite of the lowercase character classes
# refer to table 7-1 on page 189 for more character classes

# 12 days of christmas example
lyrics = '12 drummers drumming, 11 pipers piping, 10 lords a leaping, 9 ladies dancing, 8 maids a milking, 7 swans a swimming, 6 geese a laying, 5 golden rings, 4 calling birds, 3 french hens, 2 turtle doves, and 1 partridge in a pear tree'
# create a regex that matches one or more numeric digits, followed by a space, followed by one or more letters
# \d+ matches one or more numeric digits with the + character
# \s matches a space character
# \w+ matches one or more letters with the + character
xmasRegex = re.compile(r'\d+\s\w+')
mo = xmasRegex.findall(lyrics)
print(mo) # returns ['12 drummers', '11 pipers', '10 lords', '9 ladies', '8 maids', '7 swans', '6 geese', '5 golden', '4 calling', '3 french', '2 turtle', '1 partridge']

vowelRegex = re.compile(r'[aeiouAEIOU]{2}') # r'(a|e|i|o|u)' the {2} will only match 2 vowels in a row
mo = vowelRegex.findall('Robocop eats baby food. BABY FOOD.')
print(mo) 

negativeRegex = re.compile(r'[^aeiouAEIOU]') # the ^ character is used to match everything that is not in the character class
mo = negativeRegex.findall('Robocop eats baby food. BABY FOOD.')
print(mo) # finds all consonants
