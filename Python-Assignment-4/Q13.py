# ASSIGNMENT 4 - QUESTION 13
# Write a function to calculate the area of a circle.
import math

def calculate_circle_area(circle_radius):
    """Calculates and returns the area of a circle."""
    calculated_area = math.pi * (circle_radius ** 2)
    return calculated_area

radius_dimension = 7.0
area_result = calculate_circle_area(radius_dimension)

print("Circle Radius: " + str(radius_dimension))
print("Area of Circle: " + str(round(area_result, 2)))
