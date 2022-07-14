"""
File: country_stats_dec_2.py
Author: Xander Hunt
Purpose: Analyze a large CSV file (life-expectancy.csv) and come up with some stats
Exceeding requirements:
- Added ability to find results on a specific country
- Error catching for invalid years and countries
"""

# Variables
data = []
lowest = 100.0
low_point = []
highest = 0.0
high_point = []
total_ex = 0.0
count = 0

# Set up list
with open("life-expectancy.csv") as file:
    for line in file:
        words = line.strip().split(",")
        data.append(words)

# Get the inputs
response = int(input("Enter a year of interest: "))
response_2 = input("Enter a country of interest: ")
print()



""" Check for overall """
# Do the stuff with the list
for point in data:
    try:
        country = point[0]
        id = point[1]
        year = int(point[2])
        expectancy = float(point[3])
        if expectancy < lowest:
            lowest = expectancy
            low_point = point
        if expectancy > highest:
            highest = expectancy
            high_point = point
        count += 1
        total_ex += expectancy
    except:
        #print("Error")
        pass

# Calculate overall results
try:
    average = total_ex / count
except:
    pass
print(f"The overall max life expectancy is: {high_point[3]} from {high_point[0]} in {high_point[2]}")
print(f"The overall min life expectancy is: {low_point[3]} from {low_point[0]} in {low_point[2]}")
print(f"The overall average life expectancy is: {average}\n")



""" Check for specific year """
# Reset the variables
lowest = 100.0
low_point = []
highest = 0.0
high_point = []
total_ex = 0.0
count = 0

# Do the stuff with the list - specific year
for point in data:
    try:
        country = point[0]
        id = point[1]
        year = int(point[2])
        expectancy = float(point[3].strip())
        if year == response:
            if expectancy < lowest:
                lowest = expectancy
                low_point = point
            if expectancy > highest:
                highest = expectancy
                high_point = point
            count += 1
            total_ex += expectancy
    except:
        pass

# Calculate results - specific year
try:
    average = total_ex / count
    print(f"\nThe max life expectancy for the year {response} is: {high_point[3]} in {high_point[0]}")
    print(f"The min life expectancy for the year {response} is: {low_point[3]} in {low_point[0]}")
    print(f"The average life expectancy for the year {response} is: {average}\n")
except:
    print("ERROR - Chosen year")
    pass




""" Check for specific country """
# Reset the variables
lowest = 100.0
low_point = []
highest = 0.0
high_point = []
total_ex = 0.0
count = 0
check = False

# Do the stuff with the list - specific country
for point in data:
    try:
        country = point[0]
        id = point[1]
        year = int(point[2])
        expectancy = float(point[3].strip())
        if country == response_2:
            if expectancy < lowest:
                lowest = expectancy
                low_point = point
            if expectancy > highest:
                highest = expectancy
                high_point = point
            count += 1
            total_ex += expectancy
    except:
        check = True
        pass

# Calculate results - specific year
try:
    average = total_ex / count
    print(f"\nThe max life expectancy for {response_2} is: {high_point[3]} in the year {high_point[2]}")
    print(f"The min life expectancy for {response_2} is: {low_point[3]} in the year {low_point[2]}")
    print(f"The average life expectancy for {response_2} is: {average}\n")
except:
    print("ERROR - Chosen country")
    pass