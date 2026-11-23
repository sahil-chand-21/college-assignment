# ASSIGNMENT 3 - QUESTION 49
# Program to demonstrate tuple immutability and create a modified tuple using concatenation.

initial_immutable_tuple = (10, 20, 30)
additional_element_tuple = (40,)

print("Original Tuple: " + str(initial_immutable_tuple))
print("Tuples are immutable; modifying an item directly (e.g. tuple[0] = 5) raises TypeError.")

# Creating modified tuple via concatenation
modified_new_tuple = initial_immutable_tuple + additional_element_tuple
print("Modified New Tuple: " + str(modified_new_tuple))
