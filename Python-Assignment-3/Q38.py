# ASSIGNMENT 3 - QUESTION 38
# Program to remove duplicate elements from a list.

source_list_with_duplicates = [10, 20, 20, 30, 40, 10, 50, 30]

unique_elements_list = []
for current_item in source_list_with_duplicates:
    if current_item not in unique_elements_list:
        unique_elements_list.append(current_item)

print("List with Duplicates: " + str(source_list_with_duplicates))
print("Unique Elements List: " + str(unique_elements_list))
