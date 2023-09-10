import pyautogui

pyautogui.screenshot('screenshot.png') # take a screenshot and save it to the current working directory

pyautogui.locateOnScreen('screenshot.png') # returns (left, top, width, height) coordinates of first place it is found on the screen

pyautogui.locateCenterOnScreen('screenshot.png') # returns (x, y) coordinates of the center of where the image is found on the screen

pyautogui.moveTo((339, 38), duration=1) # move the mouse to the given coordinates over 1 second

pyautogui.click((339, 38)) # click the mouse at the given coordinates

