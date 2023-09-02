#** To set up the debugger on vscode you need to add a launch.json file to the .vscode folder. The launch.json file is a configuration file that tells the debugger what file to run and how to run it

# select stack, locals, source and globals when using the debugger
print('Enter the first number to add: ')
first = input()

print('Enter the second number to add: ')
second = input()

print('Enter the third number to add: ')
third = input()

print('The sum is ' + first + second + third)

#! debugger control on IDLE is a little different than VSCode, you can use the debugger control to step into, step over, step out, continue, and quit
#! you can also use the debugger control to set breakpoints, which will pause the program at a certain line of code
#! you can also use the debugger control to set a watch, which will allow you to see the value of a variable at a certain point in the program