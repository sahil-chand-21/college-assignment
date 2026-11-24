# ASSIGNMENT 4 - QUESTION 08
# Program to calculate the GCD and LCM of two numbers using mathematical functions.
import math

first_integer_value = 48
second_integer_value = 18

greatest_common_divisor = math.gcd(first_integer_value, second_integer_value)
least_common_multiple = math.lcm(first_integer_value, second_integer_value)

print("First Number: " + str(first_integer_value))
print("Second Number: " + str(second_integer_value))
print("GCD using math.gcd(): " + str(greatest_common_divisor))
print("LCM using math.lcm(): " + str(least_common_multiple))
