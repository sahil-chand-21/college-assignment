# ASSIGNMENT 2 - QUESTION 03
# Program to calculate the remainder without using the modulus operator.

dividend_number = 53
divisor_number = 7

# Formula: Remainder = Dividend - (Divisor * Quotient)
calculated_quotient = dividend_number // divisor_number
calculated_remainder = dividend_number - (divisor_number * calculated_quotient)

print("Dividend:              " + str(dividend_number))
print("Divisor:               " + str(divisor_number))
print("Calculated Remainder:  " + str(calculated_remainder))
print("Verification with %:   " + str(dividend_number % divisor_number))
