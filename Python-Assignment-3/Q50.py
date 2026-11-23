# ASSIGNMENT 3 - QUESTION 50
# Program to create two sets and perform union, intersection, difference and symmetric difference operations.

set_alpha_students = {"Aman", "Rohan", "Priya", "Sneha"}
set_beta_students = {"Priya", "Sneha", "Karan", "Deepak"}

union_result_set = set_alpha_students.union(set_beta_students)
intersection_result_set = set_alpha_students.intersection(set_beta_students)
difference_result_set = set_alpha_students.difference(set_beta_students)
symmetric_difference_set = set_alpha_students.symmetric_difference(set_beta_students)

print("Set Alpha:            " + str(set_alpha_students))
print("Set Beta:             " + str(set_beta_students))
print("Union:                " + str(union_result_set))
print("Intersection:         " + str(intersection_result_set))
print("Difference (A - B):   " + str(difference_result_set))
print("Symmetric Difference: " + str(symmetric_difference_set))
