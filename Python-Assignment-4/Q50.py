# ASSIGNMENT 4 - QUESTION 50
# Write a program to create a simple user-defined package containing two modules
# and import functions from both modules.

from math_package.arithmetic_operations import compute_sum, compute_product
from math_package.geometry_operations import compute_circle_area, compute_rectangle_perimeter

first_operand_val = 15
second_operand_val = 5
circle_radius_val = 7.0
rectangle_length_val = 10.0
rectangle_breadth_val = 6.0

sum_result_val = compute_sum(first_operand_val, second_operand_val)
product_result_val = compute_product(first_operand_val, second_operand_val)
circle_area_result = compute_circle_area(circle_radius_val)
perimeter_result = compute_rectangle_perimeter(rectangle_length_val, rectangle_breadth_val)

print("Imported functions from math_package (arithmetic_operations & geometry_operations):")
print("Sum (15 + 5): " + str(sum_result_val))
print("Product (15 * 5): " + str(product_result_val))
print("Circle Area (Radius 7.0): " + str(round(circle_area_result, 2)))
print("Rectangle Perimeter (10 x 6): " + str(perimeter_result))
