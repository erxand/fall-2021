"""
File: shopping_cart_milestone_nov13.py
Author: Xander Hunt
Purpose: Create a digital shopping cart
Creative items added:
    - Display the formatted price of the item being added along with the capitalized
    - Display name of item being deleted instead of just "item"
    - Total displayed at end of program
    - Tax calculated and added to end total (Idaho tax rate)
    - Added else statement to catch any and all invalid inputs
"""

# Start program, declare variables
print("\nWelcome to the Shopping Cart Program!")
response = ""
new_item = ""
new_item_price = 0.0
item_id = 0
cart = []
counter = 0
total = 0.0
tax = 0.0

# Set up loop, outline actions
while response != "5":
    print("""
Please select one of the following: 
    1. Add item
    2. View cart
    3. Remove item
    4. Compute total
    5. Quit""")
    response = input("Please enter an action:  ")
    print()

    # Add an item
    if response == "1":
        new_item = input("What item would you like to add?  ").capitalize()
        new_item_price = float(input(f"What is the price of '{new_item}'?  "))
        cart.append([new_item, new_item_price])
        print(f"'{new_item}' for ${new_item_price:.2f} has been added to the cart.")

    # Display cart
    elif response == "2":
        counter = 0
        for n in cart:
            print(f"{counter + 1}. {n[0]} - ${n[1]:.2f}")
            counter+= 1
    
    # Remove item, display said item name
    elif response == "3":
        item_id = int(input("Which item would you like to remove?  ")) - 1
        if 0 <= item_id < len(cart):
            print(f"{cart[item_id][0]} removed.")
            del cart[item_id]
        else:
            print("That is not a valid index, please try again and enter a number that is associated with an item.")
    
    # Calculate total
    elif response == "4":
        total = 0.0
        for i in cart:
            total += i[1]
        print(f"The total price of the items in the shopping cart is ${total:.2f}")
    
    # End loop, display total, tax, and total with tax
    elif response == "5":
        total = 0.0
        for i in cart:
            total += i[1]
        tax = total * 0.06
        print(f"""Thank you for choosing to shop with us!
The total price of the items in the cart is ${total:.2f}
The government will be robbing you an additional ${tax:.2f} as well.
This brings your total up to ${(total + tax):.2f}
Have a nice day!.""")
    
    # Catch any responses that don't fit in the 1-5 options given
    else:
        print("Please select one of the following by typing the number associated with the action.")