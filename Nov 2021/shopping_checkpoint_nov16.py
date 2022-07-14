"""
File: shopping_checkpoint_nov16.py
Author: Xander Hunt
Purpose: Mess around with lists or something
"""

# Set up some variables
response1 = ""
respone2 = ""
cart = []
counter = 0

# Create the list
print("Please enter the items of the shopping list (type: quit to finish):")
while response1 != "quit":
    response1 = input("Input: ")
    if response1 != "quit":
        cart.append(response1)

# Print the list
print("\nThe shopping list is:")
for i in cart:
    print(i)
print("\nThe shopping list with indexes is:")
for i in cart:
    print(counter, i)
    counter += 1

# Change an item
response1 = int(input("Which item would you like to change? "))
response2 = input("What is the new item? ")
cart[response1] = response2
counter = 0
print("\nThe shopping list with indexes is:")
for i in cart:
    print(counter, i)
    counter += 1