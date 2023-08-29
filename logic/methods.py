spam = ['hello', 'hi', 'howdy', 'hey']
spam.index('hello') # returns 0 for the index position hello exists at
spam.index('hey') # returns 3

# if you have DUPLICATE values in a list, the index method will return the FIRST TIME the value exists

spam = ['cat', 'dog', 'bat']
#append adds to the END of the list
spam.append('moose')
# spawn returns ['cat', 'dog', 'bat', 'moose']

# insert replaces or places the index position called (1) with the new value 'chicken'
spam.insert(1, 'chicken')
# spam returns ['cat', chicken, 'dog', 'bat']

spam = ['cat', 'dog', 'bat', 'elephant']
spam.remove('elephant')
# spam will return ['cat', 'dog', 'rat']
# remove will only remove the FIRST instance of the value so if you have 5 elephants, only the first would be deleted

del spam[0] 
#spam will return ['dog', 'rat']

spam = [2, 5, 3.14, 1]
spam.sort() # sorted using ASCII rules just like JS
#spam will return [1, 2, 3.14, 5]

spam.sort(reverse=True)
#spam will return [5, 3.14, 2, 1]

spam = ['a', 'z', 'A', 'Z']
spam.sort()
#spam will return ['A', 'Z', 'a', 'z']

# to work around the ASCII default we can use the to lowercase
spam.sort(key=str.lower)
#spam will return ['A', 'a', 'Z', 'z']
