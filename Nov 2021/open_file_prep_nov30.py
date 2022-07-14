"""
File: open_file_prep_nov30.py
Author: Xander Hunt
Purpose: Open a file and parse it or something?
"""

with open("books.txt") as books:
    for line in books:
        #print(line, end="")
        print(line.strip())

# variable.split(",") # Splis it up by commas
# variable.strip() # Takes off all the excess stuff like spaces on the end or tabs or \n or whatever