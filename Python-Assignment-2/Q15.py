# ASSIGNMENT 2 - QUESTION 15
# Program to demonstrate bitwise AND, OR and XOR operators.

bitwise_operand_one = 12  # Binary: 1100
bitwise_operand_two = 10  # Binary: 1010

bitwise_and_result = bitwise_operand_one & bitwise_operand_two  # 1000 = 8
bitwise_or_result = bitwise_operand_one | bitwise_operand_two   # 1110 = 14
bitwise_xor_result = bitwise_operand_one ^ bitwise_operand_two  # 0110 = 6

print("Operand 1: 12 (1100 in binary)")
print("Operand 2: 10 (1010 in binary)")
print("Bitwise AND (&): " + str(bitwise_and_result) + " (binary: " + bin(bitwise_and_result) + ")")
print("Bitwise OR  (|): " + str(bitwise_or_result) + " (binary: " + bin(bitwise_or_result) + ")")
print("Bitwise XOR (^): " + str(bitwise_xor_result) + " (binary: " + bin(bitwise_xor_result) + ")")
