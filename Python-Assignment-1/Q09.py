# ASSIGNMENT 1 - QUESTION 09
# Program to swap two variables using a temporary variable.

first_variable_value = 100
second_variable_value = 200

print("Before Swapping: First = " + str(first_variable_value) + ", Second = " + str(second_variable_value))

temporary_holder = first_variable_value
first_variable_value = second_variable_value
second_variable_value = temporary_holder

print("After Swapping:  First = " + str(first_variable_value) + ", Second = " + str(second_variable_value))
