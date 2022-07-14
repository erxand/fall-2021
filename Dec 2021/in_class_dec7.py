"""
File: in_class_dec7.py
Author: Xander Hunt
Purpose: He's helping the class with something they struggled with
"""

shopping_list = [
    ("Bib Shorts",          "Clothing",      92.50),
    ("Roubaix",             "Bicycle",     3599.99),
    ("Cycling Computer",    "Accessories",  394.99),
    ("Helmet",              "Accessories",  299.99),
    ("Road Shoes",          "Shoes",        144.99),
    ("700c presta tube",    "Accessories",    5.25),
    ("Jersey",              "Clothing",      25.99),
    ("Multi-Function Tool", "Accessories",   22.99),
    ("Gloves",              "Accessories",    8.99),
    ("Cleats",              "Shoes",         15.99),
    ("Power Pedals",        "Accessories",  999.99),
    ("Socks",               "Clothing",       8.50)
]

import locale
locale.setlocale(locale.LC_ALL, '')

def print_list(shopping, category):
    ''' Print out the list of the chosen category in a user-friendly way '''
    print("The list of", category, "is:\n")
    for item in shopping:
        if item[1] == category:
            print(item[0], "costs: ", 
                locale.currency(item[2], grouping=True))

"""print_list(shopping_list, "Clothing")
print()
print_list(shopping_list, "Accessories")"""

def print_total(shopping, category):
    ''' Print out the total of the whole list. '''
    total = 0
    cat_total = 0
    for item in shopping:
        total += item[2]
        if item[1] == category:
            cat_total += item[2]
    print(f"The total cost of everything is: {locale.currency(total, grouping= True)}")
    print(f"The total cost of {category} is: {locale.currency(cat_total, grouping= True)}")

def print_min_max(shopping):
    min = 100000
    min_id = []
    max = 0
    max_id = []
    for item in shopping:
            if item[2] > max:
                max = item[2]
                max_id = item
            if item[2] < min:
                min = item[2]
                min_id = item
    print(f"Cheapest item is {min_id[0]}, most expensive item is {max_id[0]}")

print_min_max(shopping_list)