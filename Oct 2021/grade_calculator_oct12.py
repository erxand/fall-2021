"""
File: grade_calculator_mar12.py
Author: Xander Hunt
Purpose: Return the letter grade after someone gives you a score.
"""

# Set up a loop for testing.
repeat = True
while repeat == True:

    # Get the number grade.
    num_grade = int(input("\n\nWhat score do you have? "))
    
    # Calculate the letter grade.
    letter_grade = "X"
    if num_grade >= 90:
        letter_grade = "n A"
    elif num_grade >= 80:
        letter_grade = " B"
    elif num_grade >= 70:
        letter_grade = " C"
    elif num_grade >= 60:
        letter_grade = " D"
    else:
        letter_grade = "n F"
    
    # Add a + or - to the grade
    last_digit = num_grade % 10
    if num_grade > 59:
        if last_digit >= 7 and num_grade < 90:
            letter_grade = letter_grade + "+"
        elif last_digit <= 3 and num_grade != 100:
            letter_grade = letter_grade + "-"
    
    # Return the letter grade.
    print(f"You got a{letter_grade} in CSE 110.")
    if num_grade < 70:
        print("Yeah so uh you failed the you should probably take that again (or not)")
    else:
        print("Hey you passed the class! Congrats man.")
    
    # See if we want to repeat.
    answer = input("Would you like to try another grade? (y/n) ")
    if answer == "y":
        print("Alright let's do it again.")
        repeat = True
    elif answer == "n":
        print("Ok have a great day!")
        repeat = False
    else:
        print("I'll take that as a no, have a great day!\n\n")
        repeat = False