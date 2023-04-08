#!/usr/bin/python3

# Import libraries
import os

# Declaration of variables
path = input("Enter a directory path: ")

# Declaration of functions
def list_files(path):
    for (root, dirs, files) in os.walk(path):
        # print the current directory path
        print("Directory:", root)

        # print the directories in the current directory
        if dirs:
            print("Subdirectories:", dirs)

        # print the files in the current directory
        if files:
            print("Files:", files)

# Main
list_files(path)

# End
