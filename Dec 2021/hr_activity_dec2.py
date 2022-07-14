"""
File: hr_activity_dec2.py
Author: Xander Hunt
Purpose: Parse a text file to a list or something
"""

# Define some variables
database = []

# Convert the text into a list of lists
with open("hr_system.txt") as file:
    for line in file:
        words = line.split(" ")
        database.append(words)

# Print everything nicely
for person in database:
    try:
        name = person[0]
        id = person[1]
        title = person[2]
        salary = float(person[3])
        paycheck = salary / 24
        if title == "Engineer":
            paycheck += 1000
        print(f"{name} (ID: {id}), {title} - ${paycheck:,.2f}")
    except:
        pass

print()