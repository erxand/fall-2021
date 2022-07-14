"""
File: loan_checkpoint_oct19.py
Author: Xander Hunt
Purpose: Figure out if someone qualifies for a loan.
"""

loan_size = 0
credit_history = 0
income_size = 0
down_payment_size = 0

# Get the input from the user.
"""print("Please answer the following questions with a rating from 1 to 10:")
loan_size = int(input("How large is the loan?\n"))
credit_history = int(input("How good is your credit history?\n"))
income_size = int(input("How high is your income?\n"))
down_payment_size = int(input("How large is the down payment?\n"))
"""

# Make a loop for proving the test cases.
loop = 1
while loop != 6:
    if loop == 1: # Case 1 functions correctly
        loan_size = 8
        credit_history = 7
        income_size = 8
        down_payment_size = 1
    elif loop == 2: # Case 2 functions correctly
        loan_size = 5
        credit_history = 2
        income_size = 7
        down_payment_size = 5
    elif loop == 3: # Case 3 functions correctly
        loan_size = 8
        credit_history = 2
        income_size = 8
        down_payment_size = 3
    elif loop == 4: # Case 4 does not function correctly
        loan_size = 2
        credit_history = 4
        income_size = 1
        down_payment_size = 7
    elif loop == 5: # Case 5 does not function correctly
        loan_size = 4
        credit_history = 5
        income_size = 5
        down_payment_size = 3
    
    # Use logic to decide if the user qualifies for the loan.
    if loan_size >= 5:
        if (credit_history >= 7) and (income_size >= 7):
            print("Yes. You qualify for the loan.")
        elif ((credit_history >= 7) or (income_size >= 7)) and (down_payment_size >= 5):
            print("Yes. You qualify for the loan.")
        else:
            print("No. You do not qualify for the loan.")
    if loan_size < 5:
        if credit_history < 4:
            print("No. You do not qualify for the loan.")
        elif (income_size >= 7) or (down_payment_size >= 7):
            print("Yes. You qualify for the loan.")
        elif (income_size >= 4) and (down_payment_size >= 4):
            print("Yes. You qualify for the loan.")
        else:
            print("No. You do not qualify for the loan.")
    loop = loop + 1