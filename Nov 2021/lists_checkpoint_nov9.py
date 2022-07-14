"""
File: lists_checkpoint_nov9.py
Author: Xander Hunt
Purpose: Make a list of names
"""

# Define variables
name = ""
friends = []

# Gather user input, add it to list
while name != "End":
    name = input("Enter the name of a friend. If no more names, enter \"end\".  ").capitalize()
    if name != "End":
        friends.append(name)

# Print out the list
print("\n")
for n in friends:
    print(n)