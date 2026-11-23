# ASSIGNMENT 3 - QUESTION 46
# Program to create a tuple and access its elements using positive and negative indexing.

engineering_branches_tuple = ("CSE", "ECE", "ME", "CE", "EE")

first_positive_element = engineering_branches_tuple[0]
third_positive_element = engineering_branches_tuple[2]
last_negative_element = engineering_branches_tuple[-1]
second_last_negative_element = engineering_branches_tuple[-2]

print("Tuple:                  " + str(engineering_branches_tuple))
print("Positive Index [0]:     " + first_positive_element)
print("Positive Index [2]:     " + third_positive_element)
print("Negative Index [-1]:    " + last_negative_element)
print("Negative Index [-2]:    " + second_last_negative_element)
