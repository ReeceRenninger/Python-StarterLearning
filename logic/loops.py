##!! while loops
spam = 0
while spam < 5:
    print('Hello, world.')
    spam = spam + 1


name = ''
while name != 'your name':
    print('Please type your name.')
    name = input()
print('Thank you!')

#break statement occurs whenever the program execution immediately jumps out of the loop
name = ''
while True:
    print('Please type your name.')
    name = input()
    if name == 'your name':
        break
print('Thank you!')

#continue statement occurs when the program execution immediately jumps back to the start of the loop and reevaluates the loop’s condition
spam = 0
while spam < 5:
    spam = spam + 1
    if spam == 3:
        continue
    print('spam is ' + str(spam))

# same as for loop below using while loop
print('My name is')
i = 0
while i < 5:
    print('Jimmy Five Times (' + str(i) + ')')
    i = i + 1

##!! for loops

print('My name is')
for i in range(5):
    print('Jimmy Five Times (' + str(i) + ')')

##!! range() function allows you to execute a for loop a certain number of times without the need to use a counter
##!! range(1, 12) is the start and end values, range(0, 10, 2) is the start, end, and step values is how much the loop increases or decreases with each iteration
total = 0
for num in range(101): # up to but not including 101
    total = total + num
print(total) # 5050
