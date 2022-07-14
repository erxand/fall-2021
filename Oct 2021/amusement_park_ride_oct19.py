"""
File: amusement_park_ride_oct19.py
Author: Xander Hunt
Purpose: Figure out if someone is allowed to go on the ride.
"""

# Get all the inputs from the user.
age_1 = int(input("What is the age of the first rider? "))
if 12 <= age_1 < 18:
    another_response = input("Do you have a golden passport? (yes/no) ")
    if another_response == "yes":
        age_1 = 18
height_1 = int(input("What is the height of the first rider? "))
age_2 = 0
height_2 = 36
another_response = input("Is there another rider? (yes/no) ")
if another_response == "yes":
    age_2 = int(input("What is the age of the second rider? "))
    if 12 <= age_2 < 18:
        another_response = input("Do you have a golden passport? (yes/no) ")
        if another_response == "yes":
            age_2 = 18
    height_2 = int(input("What is the height of the second rider? "))

# Perform the logic to check if they're allowed.
if height_1 < 36 or height_2 < 36:
    print("Sorry, you may not ride.")
elif (age_1 >= 18 and height_1 >= 62) or (age_2 >= 18 and height_2 >= 62):
    print("Welcome to the ride. Please be safe and have fun!")
elif (age_1 >= 12) and (age_2 >= 12):
    print("Welcome to the ride. Please be safe and have fun!")
elif (age_1 >= 16 and age_2 >= 14) or (age_1 >= 14 and age_2 >= 16):
    print("Welcome to the ride. Please be safe and have fun!")
else:
    print("Sorry, you may not ride.")