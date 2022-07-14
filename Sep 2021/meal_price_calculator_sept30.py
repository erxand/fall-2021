"""
File: meal_price_calculator_sept30
Author: Xander Hunt
Purpose: Take the prices of meals, number of meals, tax rate, and calculate the end costs
"""

# Stuff to add: dessert, drinks, surprise item that's super expensive

# Get the prices, number of meals, and tax rate.
child_meal_price = float(input("What is the price of a child\'s meal? "))
adult_meal_price = float(input("What is the price of an adult\'s meal? "))
number_of_children = int(input("How many children are there? "))
number_of_adults = int(input("How many adults are there? "))
tip_rate = int(input("How big of a % tip do you want to leave? (People say if you leave 20 you're a really good person) "))
sales_tax_rate = float(input("What is the sales tax rate? "))
print()

# If someone puts in a decimal for the tax or tip rates I don't want to divide it by 100, this only divides by 100 if it's less than 1.
if sales_tax_rate > 1:
    sales_tax_rate = sales_tax_rate / 100
if tip_rate > 1:
    tip_rate = tip_rate / 100

# Calculate and return the subtotal, sales tax, and total.
subtotal = (child_meal_price * number_of_children) + (adult_meal_price * number_of_adults)
tip_total = (subtotal * tip_rate)
sales_tax = (subtotal + tip_total) * sales_tax_rate
grand_total = subtotal + sales_tax + tip_total
print(f"\nSubtotal:  ${subtotal:6.2f}")
print(f"Tip:       ${tip_total:6.2f}")
print(f"Sales Tax: ${sales_tax:6.2f}")
print(f"\nTotal:     ${grand_total:6.2f}")
print()

# Get the payment amount, if it's not enough ask again, return the change. Don't forget to comment on how expensive the meal is.
cash = float(input("\nWhat is the payment amount? "))
change = cash - grand_total
while change < 0:
    print("\nHey bucko that\'s not enough cash, you gotta pay more.")
    cash = float(input("I need more money than that to pay your bill, how much are you really going to pay me? "))
    change = cash - grand_total
print(f"Your change is: ${change:6.2f}")
if grand_total > 100:
    print("Jeez man you're paying way too much for this meal!")
elif grand_total > 50:
    print("\nThat's a pretty pricey meal not gonna lie...")