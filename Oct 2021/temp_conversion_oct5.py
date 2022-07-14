"""
File: temp_conversion_oct5.py
Author: Xander Hunt
Purpose: Convert between Farenheit and Celsius
"""

# This sets up a loop so I don't have to keep clicking the run button to test multiple numbers.
again = True
while again == True:
    
    # This takes the input temp, converts it, and returns the result.
    f_temperature = float(input("What is the temperature in Fahrenheit? "))
    c_temperature = float((f_temperature - 32) * (5/9))
    print(f"The temperature in Celsius is {c_temperature:.1f} degrees.")
    
    # This checks whether to end the loop or not, and then either ends it or doesn't.
    answer = input("Would you like to do another number? (y/n) ")
    while (answer != "y") and (answer != "n"):
            answer = input("You didn't give me a \'y\' or a \'n\', please try again. ")
    if answer == "n":
        again = False
    elif answer != "y":
        again = True

# Be polite.
print("Thank you for visiting, have a nice day!")