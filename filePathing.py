import os

# os module allows you to work with files and directories on all operating systems
os.path.join('usr', 'bin', 'spam') # returns 'usr\\bin\\spam' on windows and 'usr/bin/spam' on mac and linux

os.getcwd() # returns the current working directory

os.chdir('C:\\Windows\\System32') # changes the current working directory to the one passed to it

os.getcwd() # returns the current working directory

os.chdir('C:\\Users\\Barney\\Documents\\GitHub\\automate-the-boring-stuff\\scripts') # changes the current working directory to the one passed to it

# absolute file paths begin with the root folder, C:\ on windows and / on mac and linux
# relative file paths do not begin with the root folder

os.path.abspath('.') # returns the absolute path of the argument passed to it
os.path.abspath('.\\scripts') # returns the absolute path of the argument passed to it
os.path.isabs('.') # checks if path is an absolute path, returns False

os.path.relpath('C:\\Windows', 'C:\\') # returns the relative path from the first argument to the second argument

os.path.dirname('C:\\Windows\\System32\\calc.exe') # returns the directory name of the argument passed to it

os.path.basename('C:\\Windows\\System32\\calc.exe') # returns the base name of the argument passed to it

os.path.exists('C:\\Windows\\System32\\calc.exe') # returns True if the argument passed to it exists

os.path.isfile('C:\\Windows\\System32\\calc.exe') # returns True if the argument passed to it is a file

os.path.getsize('C:\\Windows\\System32\\calc.exe') # returns the size of the file in bytes

os.listdir('C:\\Windows\\System32') # returns a list of strings of filenames for each file in the path passed to it

totalSize = 0
for filename in os.listdir('C:\\Windows\\System32'):
  if not os.path.isfile(os.path.join('C:\\Windows\\System32', filename)):
    continue
  totalSize = totalSize + os.path.getsize(os.path.join('C:\\Windows\\System32', filename))

print(totalSize) # returns byte size amount of the file directory passed to it

os.makedirs('C:\\delicious\\walnut\\waffles') # creates a new folder in the path passed to it

