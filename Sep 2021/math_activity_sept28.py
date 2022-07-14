"""
File: math_activity_sept28.py
Author: Xander Hunt
Purpose: to return the area and volume of different shapes
"""

# Get the length of the square, do the math and return the area and volume.
square_length = float(input("What is the length of a side of the square? "))
square_area = square_length ** 2
cube_volume = square_length ** 3
print(f"The area of the square is: {square_area}")
print(f"The volume of the cube is: {cube_volume}")

# Get the length and width of the rectangle, do the math and return the area.
rectangle_length = float(input("What is the length of the rectangle? "))
rectangle_width = float(input("What is the width of the rectangle? "))
rectangle_area = rectangle_length * rectangle_width
print(f"The area of the rectangle is: {rectangle_area}")

import math

# get the radius of the circle, do the math and return the area
circle_radius = float(input("What is the radius of the circle? "))
circle_area = math.pi * (circle_radius ** 2)
sphere_volume = (4 / 3) * math.pi * circle_radius ** 3
print(f"The area of the cicle is: {circle_area}")
print(f"The volume of the sphere is: {sphere_volume}")