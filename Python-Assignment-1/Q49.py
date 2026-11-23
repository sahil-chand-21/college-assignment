# ASSIGNMENT 1 - QUESTION 49
# Program to demonstrate the difference between integer and floating-point values.

integer_division_operand = 10
floating_division_operand = 10.0

integer_result = integer_division_operand // 3
floating_result = floating_division_operand / 3

print("Integer Value:               ", integer_division_operand, "Type:", type(integer_division_operand))
print("Floating-point Value:        ", floating_division_operand, "Type:", type(floating_division_operand))
print("Integer Floor Division (// 3):", integer_result, "Type:", type(integer_result))
print("Float True Division (/ 3):    ", floating_result, "Type:", type(floating_result))
