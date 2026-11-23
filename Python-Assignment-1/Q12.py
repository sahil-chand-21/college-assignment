# ASSIGNMENT 1 - QUESTION 12
# Program to calculate the area and circumference of a circle.
import math

circle_radius = 7.0

circle_area = math.pi * (circle_radius ** 2)
circle_circumference = 2 * math.pi * circle_radius

print("Circle Radius:        ", circle_radius)
print("Calculated Area:      ", round(circle_area, 2))
print("Calculated Circumference:", round(circle_circumference, 2))
