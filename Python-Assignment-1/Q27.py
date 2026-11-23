# ASSIGNMENT 1 - QUESTION 27
# Program to demonstrate the use of int(), float() and str() functions.

base_numeric_string = "75"
converted_as_int = int(base_numeric_string)
converted_as_float = float(base_numeric_string)

original_number = 3.14
converted_as_str = str(original_number)

print("Using int():  ", converted_as_int, type(converted_as_int))
print("Using float():", converted_as_float, type(converted_as_float))
print("Using str():  ", repr(converted_as_str), type(converted_as_str))
