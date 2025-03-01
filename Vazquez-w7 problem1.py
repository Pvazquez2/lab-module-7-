# Paola Vazquez
# February 26,2025
# Problem 1: Calculate the area of a circle

import math

def areaOfCircle(r):
    return math.pi * r ** 2

# Get user input and convert it to a float
radius = float(input("Enter the radius of the circle: "))

# Call the function and print the result
print(f"The area of the circle with radius {radius} is: {areaOfCircle(radius)}")
