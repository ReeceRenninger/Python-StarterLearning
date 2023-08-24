name = 'Alice'
place = 'Main Street'
time = '6 pm'
food = 'turnips'

# old way of formatting strings
print('Hello ' + name + ', you are invited to a party at ' + place + ' at ' + time + '. Please bring ' + food + '.')

# new way of formatting strings
# %s is a placeholder for a string
# %() is a tuple of values that will be inserted into the string in order
print('Hello %s, you are invited to a party at %s at %s. Please bring %s.' % (name, place, time, food))

