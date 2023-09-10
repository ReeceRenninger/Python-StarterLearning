# GUI automation (graphical user interface automation)
# using pyautogui module
# docs can be found at https://pyautogui.readthedocs.org

#! failsafe built into pyautogui to stop the program if you quickly move the mouse to the upper left corner of the screen

import pyautogui
import os

os.environ['DISPLAY'] = ':0' # this is for linux so that it knows which display to use

width, height = pyautogui.size() # returns the screen resolution
print(width)
print(height)

# move the mouse to a specific location
pyautogui.moveTo(10, 10) # move the mouse to the top left corner of the screen
pyautogui.moveTo(10, 10, duration=1.5) # move the mouse to the top left corner of the screen over 1.5 seconds

# move the mouse relative to its current position
pyautogui.moveRel(200, 0, duration=2) # move the mouse 200 pixels to the right of its current position over 2 seconds

# get mouse position
print(pyautogui.position()) # returns a tuple of the mouse's current position

pyautogui.displayMousePosition() # displays the mouse position in a pop up window

# use the click() method to click the mouse
pyautogui.click(339, 38) # click the mouse at the given coordinates

# use the rightClick() method to right click the mouse
pyautogui.rightClick(339, 38) # right click the mouse at the given coordinates

# use the doubleClick() method to double click the mouse
pyautogui.doubleClick(339, 38) # double click the mouse at the given coordinates

# use the dragTo() method to drag the mouse
pyautogui.dragTo(339, 38, duration=2) # drag the mouse to the given coordinates over 2 seconds

# use the dragRel() method to drag the mouse relative to its current position
pyautogui.dragRel(200, 0, duration=2) # drag the mouse 200 pixels to the right of its current position over 2 seconds