# similar to object key value pair system use {} to create it
myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}
myCat['size'] # returns 'fat'
'My cat has ' + myCat['color'] + ' fur.'

eggs = {'name': 'Zophie', 'species': 'cat', 'age': 8}
ham = { 'age': 8, 'name': 'Zophie', 'species': 'cat'}
eggs == ham # this will return true because order does not matter, only the key/value content

'name' in eggs # will return True
'name' not in eggs # will return False

list(eggs.keys()) # returns ['name', 'species', 'age']
list(eggs.values()) # returns ['Zophie', 'cat', 8]
list(eggs.items()) # returns [('name', 'Zophie'), ('species', 'cat'), ('age', 8)]

for k in eggs.keys():
	print(k) # returns name, species, age

for v in eggs.values():
	print(v) # returns Zophie, cat, 8

for k,v in eggs.items():
	print(k, v) # retruns name Zophie species cat age 8

for i in eggs.items():
	print(i) # returns ('name', 'Zophie') ('species', 'cat') ('age', 8)


# get() in dictionary
# takes 2 arguments key, fallback default value if does not exist
eggs.get('age', 0) # this will return 8
eggs.get('color', '') # this will return a blank string since color does not exist 

# setDefault method
if 'color' not in eggs:
	eggs['color'] = 'black'

eggs.setdefault('color', 'black') # sets a new key value pair, CAN NOT UPDATE USING THIS

# ''' triple quotes allow you to escape '' in a large string if needed '''
message = 'It was a bright cold day in April, and the clocks were stricking thirteen.'
count = {}

for character in message.upper(): # all uppercased version of this string
	count.setdefault(character, 0) # if you dont have the letter I as a key set it to 0
	count[character] = count[character] + 1 # iteratively going through the entire message and grabbing the character incrementing by 1 on each repeated character

import pprint #pretty print

pprint.pprint(count) # cleans up the format of prints to be cleaner
rjtext = pprint.pformat(count)
print(rjtext)
