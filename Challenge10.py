#!/usr/bin/python3

# Open a new file with the 'w+' mode
file = open("example.txt", "w+")

# Append three lines to the file
file.write("This is the first line.\n")
file.write("This is the second line.\n")
file.write("This is the third line.\n")

# Move the file cursor back to the start of the file
file.seek(0)

# Read and print the first line of the file
print(file.readline())

# Close the file
file.close()

# Delete the file
import os
os.remove("example.txt")
