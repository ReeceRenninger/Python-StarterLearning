#!! rules of scope
#** 1. Code in the global scope cannot use any local variables.
#** 2. Code in a local scope CAN ACCESS global variables.
#** 3. Code in one function's local scope cannot use variables in ANOTHER local scope.
#** 4. Code in one function's local scope cannot use variables in ANY other local scope.

spam = 42 #global variable

def eggs():
    spam = 42#local variable


#testing how local/global variables work

# this will not work
def spam():
    eggs = 99

spam()
print(eggs)

# eggs can be reused in different local scopes
# this will print eggs = 99 since bacon will be terminated after it is called
def spam():
    eggs = 99
    bacon()
    print(eggs)

def bacon():
    ham = 101
    eggs = 0    
spam()

# global eggs will be used
def spam():
    #no local eggs variable so global eggs will be used
    # if I wanted to change a global variable I would need to use the global keyword
    global eggs
    eggs = 'Hello'
    print(eggs)

eggs = 42
spam()


print('Some code here.')
print('Some more code.')
