# ASSIGNMENT 2 - QUESTION 29
# Program to check whether a number is divisible by 5 and 11.

tested_numeric_value = 55

is_divisible_by_both = (tested_numeric_value % 5 == 0) and (tested_numeric_value % 11 == 0)

print("Tested Number: " + str(tested_numeric_value))
if is_divisible_by_both:
    print(str(tested_numeric_value) + " is divisible by BOTH 5 and 11.")
else:
    print(str(tested_numeric_value) + " is NOT divisible by both 5 and 11.")
