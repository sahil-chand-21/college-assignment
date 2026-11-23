# ASSIGNMENT 1 - QUESTION 26
# Program to accept a number as a string and convert it into an integer.

raw_string_input = input("Enter a whole number string (default '125'): ").strip()
number_string_value = raw_string_input if raw_string_input else "125"

converted_integer_result = int(number_string_value)

print("Input as String:       ", repr(number_string_value), "Type:", type(number_string_value))
print("Converted into Integer:", converted_integer_result, "Type:", type(converted_integer_result))
