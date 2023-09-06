import pprint

cat = {'name': 'Zophie', 'age': 7, 'color': 'gray'}
allCats = []

allCats.append({'name': 'Zophie', 'age': 7, 'color': 'gray'})
allCats.append({'name': 'Pooka', 'age': 5, 'color': 'black'})
allCats.append({'name': 'Fat-tail', 'age': 5, 'color': 'gray'})
allCats.append({'name': '???', 'age': -1, 'color': 'orange'})

# this signifies the empty board for tic tac toe
theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

# print pretty version of the board
# pprint.pprint(theBoard)


# we can update the board with the following
theBoard['mid-M'] = 'X'
theBoard['top-L'] = 'O'
theBoard['top-M'] = 'O'
theBoard['top-R'] = 'O'
theBoard['mid-L'] = 'X'
theBoard['low-R'] = 'X'

pprint.pprint(theBoard)

# print the board in a more readable format
def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-----')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-----')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

printBoard(theBoard)

# the type function returns the type of the value passed to it
type(42) # returns int
type('hello') # returns str
type(3.14) # returns float
type(theBoard) # returns dict
type(theBoard['top-L']) # returns string since value at top-L is a string