"""
File: capitalization_checkpoint_dec10.py
Author: Xander Hunt
Purpose: Make some functions that capitalize strings in different ways? Aren't there already things that do that? idk man
"""

# Normal function
def display_regular(string):
    print(string)

# Uppercase function
def display_uppercase(string):
    print(string.upper())

# Lowercase function
def display_lowercase(string):
    print(string.lower())

# Get response and do stuff with it
response = input("What is your message? ")
display_regular(response)
display_uppercase(response)
display_lowercase(response)