# ASSIGNMENT 2 - QUESTION 38
# Program to calculate the sum of digits of a given number.

source_number = 4567
working_number = source_number
sum_of_individual_digits = 0

while working_number > 0:
    current_digit = working_number % 10
    sum_of_individual_digits += current_digit
    working_number //= 10

print("Given Number:   " + str(source_number))
print("Sum of Digits:  " + str(sum_of_individual_digits))
