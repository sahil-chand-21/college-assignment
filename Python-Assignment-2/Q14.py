# ASSIGNMENT 2 - QUESTION 14
# Program to check whether a number is divisible by both 3 and 5 using logical operators.

inspected_number = 30

is_divisible_by_three_and_five = (inspected_number % 3 == 0) and (inspected_number % 5 == 0)

print("Inspected Number: " + str(inspected_number))
if is_divisible_by_three_and_five:
    print("The number " + str(inspected_number) + " is divisible by both 3 and 5.")
else:
    print("The number " + str(inspected_number) + " is NOT divisible by both 3 and 5.")
