#! /usr/bin/python3

# created a file.txt in my /home/<username> directory and wrote some text in it for this program to work
# TODO: open function
testfile = open('/home/<username>/file.txt')
content = testfile.read() # returns the contents of the file
testfile.close() # closes the file #! good practice for larger files even though python will close it automatically
print(content) # prints the contents of the file to terminal

#TODO: readlines() method
testfile = open('/home/<username>/file.txt')
content = testfile.readlines() # returns a LIST of strings of each line in the file
testfile.close()
print(content) # prints the contents of the file to terminal

#TODO: write() method
testfile = open('/home/<username>/file.txt', 'w') # opens the file in write mode
testfile.write('I added this to the file using write mode, whhhhhhhaaaatttttt\n') # writes the string to the file, this overrides the previous contents of the file
testfile.close()

#TODO: whereAmI trick
# import os
# location = os.getcwd() # this can be used to be the path to the file you want to open, so you don't have to type the whole path or move the file to the same directory as the script
# print(location)

# TODO: append mode
testfile = open('/home/<username>/file.txt', 'a') # opens the file in append mode
append = testfile.write('I added this to the file using append mode, SO I DONT DELETE THE PREVIOUS CONTENTS\n') # writes to the file without overriding the previous contents
testfile.close()
print(append) 

#TODO: shelve module
import shelve
#! mydata file is created into the same directory I am working in, so it can be found in the same directory as the script you are working in if you are using vscode. If you are using the terminal, it will be in the directory you are working in.
shelfFile = shelve.open('mydata') # creates a new file named mydata.db
shelfFile['cats'] = ['Zophie', 'Pooka', 'Simon', 'Fat-tail', 'Cleo'] # creates a key named cats and assigns it a list of strings
shelfFile.close()

shelfFile = shelve.open('mydata') # opens the file
print(shelfFile['cats']) # prints the value of the key cats
shelfFile.close()

shelfFile = shelve.open('mydata') # opens the file
keys = list(shelfFile.keys()) # returns a list of the keys in the file 
print(keys)
values = list(shelfFile.values()) # returns a list of the values in the file
print(values)
shelfFile.close()
