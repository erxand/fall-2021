"""
File: windchil_calculator_dec10.py
Author: Xander Hunt
Purpose: Calculate windchill based off of temp and windspeed in F and C
"""

# Convert C to F and F to C functions
def c_to_f(numba):
    return (int(numba) * (9/5)) + 32

def f_to_c(numba):
    return (int(numba) - 32) * 5/9

# Windchill function: 35.74 + 0.6215T - 35.75(V0.16) + 0.4275T(V0.16
def windchill_f(temperature, windspeed):
    windchill = 0.0
    windchill = 35.74 + (0.6215 * temperature) - (35.75 * (windspeed ** 0.16)) + (0.4275 * temperature * (windspeed ** 0.16))
    return windchill

# Ask for inputs
temp_response = input("What is the temperature in question?  ")
type_response = input("Farenheit or Celcius? ('C' or 'F')  ")
temp_response = float(temp_response)

# Calculate and output the result
# At temperature 14.0F, and wind speed 5 mph, the windchill is: 5.93F
if type_response.upper() == "C":
    temp_response = c_to_f(temp_response)
elif type_response.upper() != "F":
    print("\n\nError in temperature scale. Please try again.\n\n")

for i in range(5, 61, 5):
    windchill = windchill_f(temp_response, i)
    print(f"At temperature {temp_response}F, and wind speed {i} mph, the windchill is: {windchill:.2f}F")