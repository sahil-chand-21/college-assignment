# ASSIGNMENT 2 - QUESTION 17
# Program to check whether a number is even or odd using a bitwise operator.

candidate_number_value = 27

# In binary, the least significant bit is 1 for odd numbers, and 0 for even numbers.
is_even_number = (candidate_number_value & 1) == 0

print("Candidate Number: " + str(candidate_number_value))
if is_even_number:
    print(str(candidate_number_value) + " is an EVEN number.")
else:
    print(str(candidate_number_value) + " is an ODD number.")
