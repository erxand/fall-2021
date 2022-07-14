"""
File: bank_account_activity_nov16.py
Author: Xander Hunt
Purpose: Practice having lists of lists
"""

# Set up variables
account = ""
amount = 0.0
accounts = []
counter = 0
total = 0.0
average = 0.0
highest = 0.0
high_index = -1

# Get user inputs
print("Enter the names and balances of bank accounts (type: quit when done)")
while account != "Quit":
    account = input("What is the name of this account? ").capitalize()
    if account != "Quit":
        amount = float(input("What is the balance? $"))
        accounts.append([account, amount])
        total += amount
        if amount > highest:
            highest = amount
for i in accounts:
    counter = 0
    if i[1] == highest:
        high_index = counter

# Print account information
print("\nAccount Information:")
counter = 0
for i in accounts:
    print(f"{counter}. {i[0]} - ${i[1]:.2f}")
    counter += 1
average = total / (len(accounts))
print(f"\nTotal: ${total:.2f}")
print(f"Average: ${average:.2f}")
print(f"Highest balance: {highest:.2f}")

# Offer to edit an account amount
response = "y"
while response == "y":
    response = input("Do you want to update an account? (y/n) ")
    if response == "y":
        response = int(input("What account index do you want to update? "))
        amount = float(input("What is the new amount? $"))
        accounts[response][1] = amount
    
    #Re-calculate the details
    total = 0.0
    highest = 0.0
    counter = 0
    for i in accounts:
        total += i[1]
        if i[1] > highest:
            highest = i[1]
            high_index = counter
        counter += 1
    average = total / len(accounts)

    # Print account information
    print("\nAccount Information:")
    for i in accounts:
        print(f"{counter}. {i[0]} - ${i[1]:.2f}")
        counter += 1
    average = total / (len(accounts))
    print(f"\nTotal: ${total:.2f}")
    print(f"Average: ${average:.2f}")
    print(f"Highest balance: {highest:.2f}")