# ASSIGNMENT 3 - QUESTION 01
# Program to accept a string and display its length.

raw_string_input = input("Enter a string (default 'Uttarakhand Technical University'): ").strip()
target_text_string = raw_string_input if raw_string_input else "Uttarakhand Technical University"

calculated_string_length = len(target_text_string)

print("Target String: " + target_text_string)
print("String Length: " + str(calculated_string_length))
