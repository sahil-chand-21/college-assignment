# ASSIGNMENT 4 - QUESTION 43
# Write a program to import the math module and calculate the square root and factorial of a number.
import math

sample_test_number = 25
factorial_target_number = 5

calculated_root_value = math.sqrt(sample_test_number)
calculated_factorial_value = math.factorial(factorial_target_number)

print("Square root of " + str(sample_test_number) + " using math.sqrt(): " + str(calculated_root_value))
print("Factorial of " + str(factorial_target_number) + " using math.factorial(): " + str(calculated_factorial_value))
