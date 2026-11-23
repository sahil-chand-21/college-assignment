# ASSIGNMENT 3 - QUESTION 31
# Program to insert an element at a specified position in a list.

programming_modules = ["Module1", "Module2", "Module4", "Module5"]
element_to_insert = "Module3"
target_insert_index = 2

print("Before Insertion: " + str(programming_modules))
programming_modules.insert(target_insert_index, element_to_insert)
print("After Insertion:  " + str(programming_modules))
