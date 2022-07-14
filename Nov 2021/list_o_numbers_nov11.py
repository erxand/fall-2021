"""
File: list_o_numbers_nov11.py
Author: Xander Hunt
Purpose: Take a list of numbers from the user and return them sorted with some stats about it.
"""

# Set up some variables
numbahs = []
response = 1
sum = 0
average = 0.0
max = 0
min = 99999

# Get inputs, add to list and sum
print("Enter a list of numbers, type 0 when finished.")
while response != 0:
    response = int(input("Enter number:  "))
    if response != 0:
        numbahs.append(response)
        sum += response

# Calculate mean, max, and min, sort the list
if sum != 0:
    average = sum / len(numbahs)
for i in numbahs:
    if i > max:
        max = i
    if i > 0 and i < min:
        min = i
numbahs.sort()

# Print the results
if sum != 0 and len(numbahs) > 1:
    print("\nSum is:", sum)
    print("Average is:", average)
    print("The largest value is:", max)
    if min != 99999:
        print("The smallest positive value is:", min)
    print("The sorted list is:")
    for i in numbahs:
        print(i)
else:
    print("\nBro that's kinda dumb, why ask for all these calculations if you're just putting a single 0 in?")