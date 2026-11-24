# ASSIGNMENT 4 - QUESTION 01
# Program to demonstrate the use of abs(), round() and pow() functions.

negative_reading_value = -48.75
decimal_precision_value = 14.6782
base_operand_value = 5
exponent_operand_value = 3

absolute_calculated_result = abs(negative_reading_value)
rounded_calculated_result = round(decimal_precision_value, 2)
power_calculated_result = pow(base_operand_value, exponent_operand_value)

print("Original Negative Value: " + str(negative_reading_value))
print("Absolute Value using abs(): " + str(absolute_calculated_result))
print("Rounded Value using round(14.6782, 2): " + str(rounded_calculated_result))
print("Power Value using pow(5, 3): " + str(power_calculated_result))
