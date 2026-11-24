# ASSIGNMENT 4 - QUESTION 04
# Program to demonstrate type conversion using int(), float() and str().

source_numeric_text = "150"
floating_point_input = 75.89
integer_counter_input = 2026

converted_integer_value = int(source_numeric_text)
converted_float_value = float(source_numeric_text)
converted_string_from_float = str(floating_point_input)
converted_string_from_int = str(integer_counter_input)

print("Original String: '" + source_numeric_text + "'")
print("Converted to int: " + str(converted_integer_value) + " (Type: " + str(type(converted_integer_value)) + ")")
print("Converted to float: " + str(converted_float_value) + " (Type: " + str(type(converted_float_value)) + ")")
print("Converted to str: '" + converted_string_from_float + "' (Type: " + str(type(converted_string_from_float)) + ")")
print("Converted to str: '" + converted_string_from_int + "' (Type: " + str(type(converted_string_from_int)) + ")")
