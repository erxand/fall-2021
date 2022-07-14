"""
File: scripture_team_activity_dec9.py
Author: Xander Hunt
Purpose: Team teach activity, something to do with books of scripture
"""

# Define list
scriptures = []

# Open file
with open("books_and_chapters.txt") as file:
    for line in file:
        line = line.split(":")
        scriptures.append(line)

# Get input to decide which book of scripture to iterate through
response = input("""Which book would you like to look at?
1 - Old Testament
2 - New Testament
3 - Book of Mormon
4 - Doctrine and Covenants
5 - Pearl of Great Price
""")

# Define function to print results of iteration
def print_results(desired_book):
    max_chap = 0
    max_book = ""
    for book in scriptures:
        if book[2].strip() == desired_book:
            print(f"Scripture: {book[2].strip()}, Book: {book[0]}, Chapters: {book[1]}")
            if int(book[1]) > max_chap:
                try:
                    max_chap = int(book[1])
                    max_book = book[0]
                except:
                    print("error, sorry bro")
    print(f"\nThe book with the most chapters in the {desired_book} is {max_book} with {max_chap} chapters.")

# Call the correct book based on input
match response:
    case "1":
        print_results("Old Testament")
    case "2":
        print_results("New Testament")
    case "3":
        print_results("Book of Mormon")
    case "4":
        print_results("Doctrine and Covenants")
    case "5":
        print_results("Pearl of Great Price")