# User-defined module for Question 42
# Contains functions for basic arithmetic operations.

def perform_addition(first_number, second_number):
    return first_number + second_number

def perform_subtraction(first_number, second_number):
    return first_number - second_number

def perform_multiplication(first_number, second_number):
    return first_number * second_number

def perform_division(first_number, second_number):
    if second_number != 0:
        return first_number / second_number
    return "Error: Division by zero is undefined"
