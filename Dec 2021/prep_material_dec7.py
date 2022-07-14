"""
File: prep_material_dec7.py
Author: Xander Hunt
Purpose: Prove that I can sort through text to find the item with the lowest/highest number
"""

min = 100
counter = 0
id = 0

people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]

people_v2 = []

for person in people:
    people_v2.append(person.split(" "))

for person in people_v2:
    if int(person[1]) < min:
        min = int(person[1])
        id = counter
    counter += 1

print()
print(people_v2[id][0], min)
print()