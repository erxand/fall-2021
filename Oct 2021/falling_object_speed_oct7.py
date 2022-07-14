"""
File: falling_object_speed_oct7.py
Author: Xander Hunt
Purpose: To calculate the speed of a falling object.
"""

# Get all the input data from the user.
print("Welcome to the velocity calculator. Please enter the following: \n")
mass = float(input("Mass (in kg): "))
gravity_acceleration = float(input("Gravity (in m/s^2, 9.8 for Earth, 24 for Jupiter): "))
time = float(input("Time (in seconds): "))
fluid_density = float(input("Density of the fluid (in kg/m^3, 1.3 for air, 1000 for water): "))
area = float(input("Cross sectional area (in m^2): "))
drag_constant = float(input("Drag constand (0.5 for sphere, 1.1 for cylinder): "))
print()

# Import math and calculate the results.
import math
value_of_c = 0.5 * fluid_density * area * drag_constant
velocity_at_t = math.sqrt((mass * gravity_acceleration)/value_of_c) * (1 \
    - math.exp((-math.sqrt(mass * gravity_acceleration * value_of_c)/mass) * time))

# Return the results.
print(f"The inner value of c is: {value_of_c:.3f}")
print(f"The velocity after {time} seconds is: {velocity_at_t:.3f}")
print("\nHope this helped, have a great day!")