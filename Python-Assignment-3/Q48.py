# ASSIGNMENT 3 - QUESTION 48
# Program to demonstrate tuple concatenation, repetition and slicing.

tuple_alpha = (1, 2, 3)
tuple_beta = (4, 5, 6)

concatenated_tuple = tuple_alpha + tuple_beta
repeated_tuple = tuple_alpha * 3
sliced_tuple = concatenated_tuple[1:5]

print("Tuple 1:        " + str(tuple_alpha))
print("Tuple 2:        " + str(tuple_beta))
print("Concatenated:   " + str(concatenated_tuple))
print("Repeated (* 3): " + str(repeated_tuple))
print("Sliced [1:5]:   " + str(sliced_tuple))
