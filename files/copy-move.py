import shutil

#TODO: Copy File
shutil.copy('/home/<username>/file.txt', '/home/<username>/copyFile.txt') # copies the file content to the new file path 
# this could also be used to copy a file to a new DIRECTORY 

shutil.copy('/home/<username>/file.txt', '/home/<username>/CopiedStuff/newFileName.txt') # copies the file into a new directory AND renames the file

#TODO: Copy Directory
shutil.copytree('home/<username>/CopiedStuff', 'home/<username>/CopiedStuffBackup') # copies the directory and all of its contents to the new directory

#TODO: Move File
shutil.move('/home/<username>/file.txt', '/home/<username>/CopiedStuff') # moves the file to the new directory

# TODO: Rename File
shutil.move('/home/<username>/file.txt', '/home/<username>/fileRenamed.txt') # NO RENAME FUNCTION EXISTS so we use move by moving it to the same directory with a new name

