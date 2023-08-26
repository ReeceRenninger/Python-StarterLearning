import re

# both of these are the same, but the second one is more readable and easier to understand with how it groups the regex
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242.')
print(mo.group())
# prints the first set of digits
print('first set of digits ' + mo.group(1))
# prints the second set of digits
print('second set of digits ' + mo.group(2))

# the different regex style in the compile method is what gives the print statement the parentheses around the area code and only the hyphen between the remaining numbers
phoneNumRegex = re.compile(r'\(\d\d\d\) \d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is (415) 555-4242.')
print(mo.group())

# the pipe character is used to match one of many expressions as part of the regex
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group())




