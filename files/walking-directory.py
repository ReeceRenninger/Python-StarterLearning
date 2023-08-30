import os
import shutil 

#! BE MINDFUL OF WHERE YOU CALL THIS IN THE FILE SYSTEM WHEN USING THIS FUNCTION
#TODO: Walking a Directory Tree, this can be great for deleting files or folders that you don't want anymore as well as copying or moving files or folders if you have a lot of them
for folder_name, sub_folders, file_names in os.walk('/home/<username>/'): # returns a generator object that can be iterated through
      print(f'The current folder is {folder_name}') # prints the current folder
      print(f'The subfolders in {folder_name} are: {sub_folders}') # prints the subfolders in the current folder
      print(f'The filenames in {folder_name} are: {file_names}') # prints the filenames in the current folder
      print() # prints a blank line

      for sub_folder in sub_folders: # iterates through the subfolders
            if 'fish' in sub_folder: # checks if fish is in the subfolder name
                  os.rmdir(sub_folder) # deletes the subfolder if fish is in the name
      for file_name in file_names:
            if file_name.endswith('.py'):
                  shutil.copy(os.join(folder_name, file_name), os.join(folder_name, file_name + '.backup'))
