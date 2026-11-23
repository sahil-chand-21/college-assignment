# ASSIGNMENT 2 - QUESTION 10
# Program to calculate the sum of the digits of a two-digit number.

two_digit_number = 87

tens_place_digit = two_digit_number // 10
units_place_digit = two_digit_number % 10
sum_of_two_digits = tens_place_digit + units_place_digit

print("Two Digit Number: " + str(two_digit_number))
print("Tens Digit:       " + str(tens_place_digit))
print("Units Digit:      " + str(units_place_digit))
print("Sum of Digits:    " + str(sum_of_two_digits))
