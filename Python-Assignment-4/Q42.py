# ASSIGNMENT 4 - QUESTION 42
# Write a program to create a module containing functions for addition, subtraction,
# multiplication and division.

import arithmetic_module

operand_number_one = 30
operand_number_two = 6

print("Imported arithmetic_module successfully.")
print("Operand 1: " + str(operand_number_one) + ", Operand 2: " + str(operand_number_two))
print("Addition:       " + str(arithmetic_module.perform_addition(operand_number_one, operand_number_two)))
print("Subtraction:    " + str(arithmetic_module.perform_subtraction(operand_number_one, operand_number_two)))
print("Multiplication: " + str(arithmetic_module.perform_multiplication(operand_number_one, operand_number_two)))
print("Division:       " + str(arithmetic_module.perform_division(operand_number_one, operand_number_two)))
