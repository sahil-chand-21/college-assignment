# ASSIGNMENT 2 - QUESTION 06
# Program to demonstrate the difference between / and // operators.

numerator_value = 17
denominator_value = 4

true_floating_division = numerator_value / denominator_value
floor_integer_division = numerator_value // denominator_value

print("Numerator:              " + str(numerator_value))
print("Denominator:            " + str(denominator_value))
print("True Division (/):      " + str(true_floating_division) + " (returns float)")
print("Floor Division (//):    " + str(floor_integer_division) + " (returns integer)")
