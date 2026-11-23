# ASSIGNMENT 1 - QUESTION 10
# Program to swap two variables without using a temporary variable.

first_variable_value = 55
second_variable_value = 99

print("Before Swapping: First = " + str(first_variable_value) + ", Second = " + str(second_variable_value))

first_variable_value, second_variable_value = second_variable_value, first_variable_value

print("After Swapping:  First = " + str(first_variable_value) + ", Second = " + str(second_variable_value))
