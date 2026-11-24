# ASSIGNMENT 4 - QUESTION 44
# Write a program to demonstrate importing a specific function from a module.

from math import sqrt, pi

circle_radius_length = 5.0
hypotenuse_squared_value = 169.0

calculated_hypotenuse = sqrt(hypotenuse_squared_value)
calculated_circle_area = pi * (circle_radius_length ** 2)

print("Demonstrating specific function import: 'from math import sqrt, pi'")
print("Square Root of 169.0: " + str(calculated_hypotenuse))
print("Area of Circle (Radius 5.0): " + str(round(calculated_circle_area, 2)))
