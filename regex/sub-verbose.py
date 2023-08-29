import re

namesRegex = re.compile(r'Agent \w+') # \w means any letter, digit, or underscore
print(namesRegex.findall('Agent Alice gave the secret documents to Agent Bob.')) # returns ['Agent Alice', 'Agent Bob']

# .sub method replaces all instances of the first argument, 'Agent', with the second argument, 'REDACTED' 
secret = namesRegex.sub('REDACTED', 'Agent Alice gave the secret documents to Agent Bob.')
print(secret) # returns REDACTED gave the secret documents to REDACTED.

# \1 means the first group in the regex, \2 means the second group in the regex, and so on
namesRegex = re.compile(r'Agent (\w)\w*') # \w means any letter, digit, or underscore with * meaning zero or more times
print(namesRegex.findall('Agent Alice gave the secret documents to Agent Bob.')) # returns ['A', 'B']
print(namesRegex.sub(r'Agent \1****', 'Agent Alice gave the secret documents to Agent Bob.')) # returns 'Agent A**** gave the secret documents to Agent B****.'

# re.VERBOSE allows you to add whitespace and comments to the string passed to re.compile()
# this allows you to make the regex more readable
# this is useful for complex regexes
# # can be used to add notes to the regex
re.compile(r'''
           (\d\d\d-) | # area code (without parens, with dash)
            (\(\d\d\d\) ) # -or- area code with parens and no dash             
           \d\d\d # first 3 digits
           -      # second dash
           \d\d\d\d # last 4 digits
           \sx\d{2,4} # extension, like''', re.IGNORECASE | re.DOTALL | re.VERBOSE) 

# re.IGNORECASE or re.I makes the regex case-insensitive
# re.DOTALL or re.S makes the . character match all characters, including newline characters
# re.VERBOSE or re.X allows you to add whitespace and comments to the string passed to re.compile()


