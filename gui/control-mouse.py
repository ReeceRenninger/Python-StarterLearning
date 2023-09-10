# GUI automation (graphical user interface automation)
# using pyautogui module
# docs can be found at https://pyautogui.readthedocs.org

import pyautogui
import os

os.environ['DISPLAY'] = ':0' # this is for linux so that it knows which display to use

width, height = pyautogui.size() # returns the screen resolution
print(width)
print(height)