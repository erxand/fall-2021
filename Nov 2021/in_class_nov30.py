"""
File: open_file_prep.py
Author: Xander Hunt
Purpose: Open a file and parse it or something?
"""
# Add some spacing to make it pretty
from typing import MutableMapping


print("\n\n\n")

# Open data.txt
with open("data.txt") as file:
    
    # Go through the file
    for line in file:
        words = line.split(":")
        #print(words)

        try: # This is thrown in there to to catch exceptions
            name = words[0].strip()
            age = int(words[1].strip())
            gender = words[2].strip()
            print(f"Name: {name}  Age: {age}  Gender: {gender}")
        except: # This is what is run every time that an exception is run into
            pass