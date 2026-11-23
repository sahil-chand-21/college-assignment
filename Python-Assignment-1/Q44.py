# ASSIGNMENT 1 - QUESTION 44
# Program to accept two numbers from the user and display their sum.

first_number_input = input("Enter first number (default 25): ").strip()
first_number_value = float(first_number_input) if first_number_input else 25.0

second_number_input = input("Enter second number (default 35): ").strip()
second_number_value = float(second_number_input) if second_number_input else 35.0

calculated_sum_result = first_number_value + second_number_value

print("Sum of " + str(first_number_value) + " and " + str(second_number_value) + " is: " + str(calculated_sum_result))
