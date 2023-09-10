import pyautogui

pyautogui.click(100, 100); pyautogui.typewrite('Hello world!', interval=0.2) # type with quarter-second pause in between each key, click the mouse at the given coordinates and type 'Hello world!'

pyautogui.typewrite(['a', 'b', 'left', 'left', 'X', 'Y'], interval=1) # press the A key, then the B key, then left arrow key twice, then type 'XY'

pyautogui.press('f1') # press the F1 key

pyautogui.hotkey('ctrl', 'o') # press the ctrl + o hotkey

