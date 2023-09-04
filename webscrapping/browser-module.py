#!/usr/bin/env python3

import webbrowser, sys, pyperclip

sys.argv

# check if command line arguments were passed
if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:]) # 1: to ignore the first argument
elif len(pyperclip.paste()) > 1:
    address = pyperclip.paste()
else:
    print('Usage: python3 browser-module.py [address]')
    sys.exit()

url = ('https://www.google.com/maps/place/' + address)

webbrowser.open(url)

