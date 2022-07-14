"""
File: guess_numer_oct_26.py
Author: Xander Hunt
Purpose: Make a number guessing game where the computer responds with "higher" or "lower" when the user guesses incorrectly
"""

# Start up the replayable loop and get stuff set up.
seguir = True
import random
while seguir:

    # Get the beginning going, set up variables.
    print("\n\nNew Game")
    min = int(input("What is the minimum value you'd like to guess from? "))
    max = int(input("What is the maximum value you'd like to guess from? "))
    answer = random.randint(min, max)
    guess = 0
    count = 0

    # Guessing loop.
    while answer != guess:
        guess = int(input("What is the magic number? "))
        if answer == guess:
            print(f"\nCongratulations! You got it! The answer was {answer}!")
        elif answer < guess:
            print(f"\nThe answer is lower than {guess}.")
        elif answer > guess:
            print(f"\nThe answer is higher than {guess}.")
        count += 1
    
    # Feedback, ask if replay is desired and perform logic for said answer.
    print(f"\nIt took you {count} guesses.")
    respuesta = input("Would you like to play again? (y/n) ")
    if respuesta != "y":
        seguir = False
    else:
        print("Alrighty let's play again.")

# Display an end message.
print("\nThat's all, have a nice day.")