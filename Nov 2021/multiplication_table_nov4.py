"""
File: multiplication_table_nov4.py
Author: Xander Hunt
Purpose: Create a multiplication table
Bridgekeeper is the code
"""

# Get the input and define variables.
colrow = int(input("How many columns and rows do you want in your multiplication table?  "))
bigvalue = colrow * colrow
colrow += 1
width = len(str(bigvalue)) + 1
result = 0

# Create the table.
for col in range(1, colrow):
    for row in range(1, colrow):
        result = col * row
        print(f"{result:{width}}", sep= " ", end= "")
    print()