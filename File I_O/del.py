"""
using the os module
Module(like a code library) is a file written by another programmer that generally has a functions we can use.

"""

import os
#os.remove("dell.txt")  # This will remove the file named dell.txt if it exists. If it doesn't exist, it does nothing.
print(os.name)  # output: posix or nt (for windows)

# getting directory information
print("Current working directory: ", os.getcwd())
print()
print("List of files and directories in the current directory: ", os.listdir())
print()

"""
# creating, deleting and renaming directories
os.mkdir("new_dir")  # creates a new directory in the current working directory
os.rmdir("new_dir")  # removes that directory
os.rename("old_dir", "new_dir")  # renames a directory from old_dir to new_dir
# getting file information

print(os.path.isfile("with_data.txt"))  # returns True if the file exists
print(os.path.isdir("with_data.txt"))  # returns True if the directory exists
print(os.path.abspath("with_data.txt"))  # returns the absolute path of the file
print(os.path.isabs("with_data.txt"))  # returns True if the path is an absolute path

print(os.path.isabs(os.path.abspath("with_data.txt")))  # returns True
print(os.path.getsize("with_data.txt"))  # returns the size of the file in bytes
print(os.path.getmtime("with_data.txt"))  # returns the time when the file was last modified
import datetime
print(datetime.datetime.fromtimestamp(os.path.getmtime("with_data.txt")))  # returns the time in a readable format

"""