import os

# TODO: unlink deletes a single file in the cwd
os.unlink('someFileName.txt') # deletes the file passed to it

# TODO: rmdir
os.rmdir('someFolderName') # deletes the folder passed to it, folder must be empty

import shutil

# TODO: remove directory and all of its contents
shutil.rmtree('someFolderName') # deletes the folder passed to it and all of its contents

#! DRY RUN EXAMPLE
for filename in os.listdir():
  if filename.endswith('.rxt'):
    # os.unlink(filename) #! uncomment this line to delete all files that end with .rxt in the cwd
    print(filename) # this tells you what will be deleted without actually deleting it

# TODO: send2trash 3rd party module
# use pipinstall send2trash to install
import send2trash

send2trash.send2trash('someFileName.txt') # sends the file to the trash bin instead of deleting it permanently