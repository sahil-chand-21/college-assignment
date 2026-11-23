# ASSIGNMENT 2 - QUESTION 13
# Program to check whether a number lies between 10 and 100 using logical operators.

tested_number_value = 45

is_in_specified_range = (tested_number_value >= 10) and (tested_number_value <= 100)

print("Tested Number: " + str(tested_number_value))
if is_in_specified_range:
    print("The number " + str(tested_number_value) + " lies between 10 and 100.")
else:
    print("The number " + str(tested_number_value) + " does not lie between 10 and 100.")
