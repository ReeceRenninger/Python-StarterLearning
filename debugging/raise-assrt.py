# TODO: raise
# custom error message
# raise Exception('This is the error message.')
import traceback # this allows us to get the error message as a string value



def boxPrint(symbol, width, height):
    if len(symbol) != 1: # check if the symbol is a single character
        raise Exception('Symbol must be a single character string.')
    if (width < 2) or (height < 2): # check if the width and height are at least 2
        raise Exception('Width and height must be greater or equal to 2.')
    print(symbol * width)
    for i in range(height - 2): # -2 because we don't want the top and bottom of the box to be printed twice
        print(symbol + (' ' * (width - 2)) + symbol) # print the sides of the box
    print(symbol * width) # print the bottom of the box

boxPrint('*', 15, 5)

# traceback example 
# try 
#     raise Exception('This is the error message.')
# except:
#     errorFile = open('error_log.txt', 'a') # open the file in append mode
#     errorFile.write(traceback.format_exc()) # write the error message to the file
#     errorFile.close()
#     print('The traceback info was written to error_log.txt.')

# assertions: are used to check that something is true at a specific point in the program
# assert False, 'This is the error message.' # this will always fail and print the error message

market_2nd = {'ns': 'green', 'ew': 'red'}

def switchLights(intersection):
    for key in intersection.keys():
        if intersection[key] == 'green':
            intersection[key] = 'yellow'
        elif intersection[key] == 'yellow':
            intersection[key] = 'red'
        elif intersection[key] == 'red':
            intersection[key] = 'green'
    assert 'red' in intersection.values(), 'Neither light is red!' + str(intersection)
print(market_2nd)
switchLights(market_2nd)
print(market_2nd)