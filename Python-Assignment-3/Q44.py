# ASSIGNMENT 3 - QUESTION 44
# Program to copy one list into another and demonstrate the difference between copy() and direct assignment.

original_data_list = [10, 20, 30]

# Direct assignment (alias reference)
assigned_reference_list = original_data_list

# Shallow copy using copy()
independent_copied_list = original_data_list.copy()

# Modify original list
original_data_list.append(40)

print("Original List after modifying: " + str(original_data_list))
print("Assigned List (reflects change):" + str(assigned_reference_list))
print("Copied List (remains separate): " + str(independent_copied_list))
