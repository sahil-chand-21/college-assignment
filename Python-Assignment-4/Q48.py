# ASSIGNMENT 4 - QUESTION 48
# Write a program to use the math module to calculate the value of a mathematical expression.
# Expression: sqrt(x^2 + y^2) + e^(sin(angle))
import math

coordinate_horizontal = 3.0
coordinate_vertical = 4.0
given_angle_radians = math.radians(30.0)

# Evaluate: sqrt(3^2 + 4^2) + exp(sin(30 degrees))
hypotenuse_part = math.sqrt((coordinate_horizontal ** 2) + (coordinate_vertical ** 2))
exponential_part = math.exp(math.sin(given_angle_radians))
total_expression_result = hypotenuse_part + exponential_part

print("Horizontal Coordinate: " + str(coordinate_horizontal))
print("Vertical Coordinate:   " + str(coordinate_vertical))
print("Expression: sqrt(x^2 + y^2) + exp(sin(30°))")
print("Evaluated Result: " + str(round(total_expression_result, 4)))
