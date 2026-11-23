# ASSIGNMENT 2 - QUESTION 36
# Program to reverse a given integer using a while loop.

original_number_value = 12345
remaining_number = original_number_value
reversed_number_result = 0

while remaining_number > 0:
    extracted_unit_digit = remaining_number % 10
    reversed_number_result = (reversed_number_result * 10) + extracted_unit_digit
    remaining_number //= 10

print("Original Number: " + str(original_number_value))
print("Reversed Number: " + str(reversed_number_result))
