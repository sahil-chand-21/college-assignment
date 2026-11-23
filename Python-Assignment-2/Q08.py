# ASSIGNMENT 2 - QUESTION 08
# Program to swap two numbers using arithmetic operators.

first_swap_number = 35
second_swap_number = 75

print("Before Swapping: First = " + str(first_swap_number) + ", Second = " + str(second_swap_number))

first_swap_number = first_swap_number + second_swap_number
second_swap_number = first_swap_number - second_swap_number
first_swap_number = first_swap_number - second_swap_number

print("After Swapping:  First = " + str(first_swap_number) + ", Second = " + str(second_swap_number))
