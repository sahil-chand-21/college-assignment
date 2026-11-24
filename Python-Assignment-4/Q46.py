# ASSIGNMENT 4 - QUESTION 46
# Write a program to demonstrate importing a module using an alias.

import math as mathematical_library

radius_measurement = 10.0
circumference_calculation = 2 * mathematical_library.pi * radius_measurement

print("Demonstrating alias import: 'import math as mathematical_library'")
print("Radius: " + str(radius_measurement))
print("Circumference using alias: " + str(round(circumference_calculation, 2)))
