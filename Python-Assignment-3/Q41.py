# ASSIGNMENT 3 - QUESTION 41
# Program to demonstrate list slicing with different index ranges.

alphabet_sequence = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

slice_first_three = alphabet_sequence[0:3]
slice_middle_four = alphabet_sequence[2:6]
slice_with_step = alphabet_sequence[::2]
slice_reversed = alphabet_sequence[::-1]

print("Original List:    " + str(alphabet_sequence))
print("First 3 elements: " + str(slice_first_three))
print("Middle [2:6]:     " + str(slice_middle_four))
print("Every 2nd step:   " + str(slice_with_step))
print("Reversed slice:   " + str(slice_reversed))
