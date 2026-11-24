# ASSIGNMENT 4 - QUESTION 41
# Write a Python program to create a user-defined module containing a function to calculate
# the square of a number and import it into another program.

import square_module

input_value_to_square = 9

calculated_square_result = square_module.calculate_square_of_number(input_value_to_square)

print("Imported square_module successfully.")
print("Given Number: " + str(input_value_to_square))
print("Square using square_module.calculate_square_of_number(): " + str(calculated_square_result))
