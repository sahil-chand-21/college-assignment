# ASSIGNMENT 2 - QUESTION 19
# Program to demonstrate identity operators is and is not.

first_numbers_list = [10, 20, 30]
second_numbers_list = [10, 20, 30]
alias_reference_list = first_numbers_list

print("List 1 identity vs List 2 identity (same content, different objects):")
print("first_numbers_list is second_numbers_list:     " + str(first_numbers_list is second_numbers_list))
print("first_numbers_list is not second_numbers_list: " + str(first_numbers_list is not second_numbers_list))

print("\nList 1 identity vs alias reference (same object reference):")
print("first_numbers_list is alias_reference_list:    " + str(first_numbers_list is alias_reference_list))
