# ASSIGNMENT 3 - QUESTION 04
# Program to reverse a string without using built-in reverse functions.

original_text_sequence = "Algorithm Design"
reversed_text_sequence = ""

for character_index in range(len(original_text_sequence) - 1, -1, -1):
    reversed_text_sequence += original_text_sequence[character_index]

print("Original String: " + original_text_sequence)
print("Reversed String: " + reversed_text_sequence)
