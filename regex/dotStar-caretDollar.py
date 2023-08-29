import re

beginsWIthHello = re.compile(r'^Hello') # ^ means begins with
print(beginsWIthHello.search('Hello world!')) # returns a match object
print(beginsWIthHello.search('He said hello.')) #returns None

endsWithWorldRegex = re.compile(r'world!$') # $ means ends with
print(endsWithWorldRegex.search('Hello world!')) # returns a match object
print(endsWithWorldRegex.search('Hello world! Hello')) # returns None

allDigitsRegex = re.compile(r'^\d+$') # ^ means begins with, $ means ends with, \d+ means one or more digits
print(allDigitsRegex.search('1234567890')) # returns a match object
print(allDigitsRegex.search('12345xyz67890')) # returns None because it has letters in it

atRegex = re.compile(r'.at') # . means any character except newline
mo = atRegex.findall('The cat in the hat sat on the flat mat.') 
print(mo)# returns ['cat', 'hat', 'sat', 'lat', 'mat']


nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)') # .* means any character except newline, * means zero or more times
mo = nameRegex.findall('First Name: Al Last Name: Sweigart')
print(mo) # returns [('Al', 'Sweigart')]

serve = '<To serve humans> for dinner.>'
nongreedy = re.compile(r'<(.*?)>') 
mo = nongreedy.findall(serve)
print(mo) # returns ['To serve humans']

greedy = re.compile(r'<(.*)>')
mo = greedy.findall(serve)
print(mo) # returns ['To serve humans> for dinner.']

prime = 'Serve the public trust.\nProtect the innocent.\nUpload the law.' # \n means newline
dotStar = re.compile(r'.*')
mo = dotStar.search(prime)
print(mo) # returns <_sre.SRE_Match object; span=(0, 23), match='Serve the public trust.'>
dotStar = re.compile(r'.*', re.DOTALL) # re.DOTALL means . matches all characters, including newline characters
mo = dotStar.search(prime)
print(mo) # returns <_sre.SRE_Match object; span=(0, 61), match='Serve the public trust.\nProtect the innocent.\nU>

vowelRegex = re.compile(r'[aeiou]') # [aeiou] means match any vowel
print(vowelRegex.findall('Al, why does your programming book talk about RoboCop so much?')) # returns ['o', 'e', 'o', 'u', 'o', 'a', 'a', 'o', 'a', 'o', 'o', 'u', 'o', 'u']

vowelRegex = re.compile(r'[aeiou]', re.I) # re.I means case-insensitive
print(vowelRegex.findall('Al, why does your programming book talk about RoboCop so much?')) # returns ['A', 'o', 'e', 'o', 'u', 'o', 'a', 'a', 'o', 'a', 'o', 'o', 'u', 'o', 'u']
