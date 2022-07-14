"""
File: proof_of_concept.py
Author: Xander Hunt
Purpose: Prove my theory of automated day-trading
"""

# Set up variables
beginning_input = float(input("How much money will you start with?  $"))
running_total = beginning_input
increase_per_minute = 0.0001
b1 = True
b2 = True
b3 = True
b4 = True
b5 = True
b6 = True
b7 = True
b8 = True

"""
# Do calculations and print results - 1 hour
for i in range(60):
    running_total += running_total * increase_per_minute
print(f"Total after 1 hour: ${running_total:,.2f}")

running_total = beginning_input
# Do calculations and print results - 1 day
for i in range(24):
    for i in range(60):
        running_total += running_total * increase_per_minute
print(f"Total after 1 day: ${running_total:,.2f}")

running_total = beginning_input
# Do calculations and print results - 1 week
for i in range(7):
    for i in range(24):
        for i in range(60):
            running_total += running_total * increase_per_minute
print(f"Total after 1 week: ${running_total:.2f}")

running_total = beginning_input
# Do calculations and print results - 1 month
for i in range(4):
    for i in range(7):
        for i in range(24):
            for i in range(60):
                running_total += running_total * increase_per_minute
print(f"Total after 1 month: ${running_total:,.2f}")

running_total = beginning_input
# Do calculations and print results - 3 months
for i in range(3):
    for i in range(4):
        for i in range(7):
            for i in range(24):
                for i in range(60):
                    running_total += running_total * increase_per_minute
print(f"Total after 3 months: ${running_total:,.2f}")"""


running_total = beginning_input
# Do calculations and print results - other
for month in range(12):
    for week in range(4):
        for day in range(7):
            for hour in range(24):
                for min in range(60):
                    running_total += running_total * increase_per_minute
                    if 1000 <= running_total and b1:
                        print(f"You will have $1,000 after {month} months, {week} weeks, {day} days, {hour} hours, and {min} minutes")
                        b1 = False
                    if running_total >= 10000 and b2:
                        print(f"You will have $10,000 after {month} months, {week} weeks, {day} days, {hour} hours, and {min} minutes")
                        b2 = False
                    if running_total >= 100000 and b3:
                        print(f"You will have $100,000 after {month} months, {week} weeks, {day} days, {hour} hours, and {min} minutes")
                        b3 = False
                    if running_total >= 500000 and b4:
                        print(f"You will have $500,000 after {month} months, {week} weeks, {day} days, {hour} hours, and {min} minutes")
                        b4 = False
                    if running_total >= 1000000 and b5:
                        print(f"You will have 1 million after {month} months, {week} weeks, {day} days, {hour} hours, and {min} minutes")
                        b5 = False
                    if running_total >= 100000000 and b6:
                        print(f"You will have 100 million after {month} months, {week} weeks, {day} days, {hour} hours, and {min} minutes")
                        b6 = False
                    if running_total >= 500000000 and b7:
                        print(f"You will have 500 million after {month} months, {week} weeks, {day} days, {hour} hours, and {min} minutes")
                        b7 = False
                    if running_total >= 1000000000 and b8:
                        print(f"You will have 1 billion after {month} months, {week} weeks, {day} days, {hour} hours, and {min} minutes")
                        b8 = False