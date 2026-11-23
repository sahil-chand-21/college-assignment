# ASSIGNMENT 3 - QUESTION 25
# Program to check whether two strings are equal, ignoring their case.

first_comparison_text = "Python Programming"
second_comparison_text = "PYTHON PROGRAMMING"

are_strings_case_insensitively_equal = (first_comparison_text.lower() == second_comparison_text.lower())

print("String 1: " + first_comparison_text)
print("String 2: " + second_comparison_text)
print("Equal ignoring case: " + str(are_strings_case_insensitively_equal))
