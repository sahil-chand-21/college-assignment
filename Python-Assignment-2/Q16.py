# ASSIGNMENT 2 - QUESTION 16
# Program to demonstrate left-shift and right-shift operators.

original_bit_value = 8
shift_positions_count = 2

left_shifted_result = original_bit_value << shift_positions_count   # Multiplies by 2^2 = 32
right_shifted_result = original_bit_value >> shift_positions_count  # Divides by 2^2 = 2

print("Original Value:   " + str(original_bit_value))
print("Left Shift (<< 2):  " + str(left_shifted_result))
print("Right Shift (>> 2): " + str(right_shifted_result))
