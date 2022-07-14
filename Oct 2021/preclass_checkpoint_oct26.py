"""
File: preclass_checkpoint_oct26.py
Author: Xander Hunt
Purpose: Prove that I'm not completely incompetent with while loops.
"""

response = float(input("Please enter a positive number: "))

while response < 0:
    response = float(input("That is a negative number, please enter a positive number: "))

response = input("May I have a piece of candy? ")

while response.lower() != "yes":
    response = input("May I please have a piece of candy? ")

print("Have a great day!")