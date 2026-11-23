# ASSIGNMENT 3 - QUESTION 40
# Program to find common elements between two lists.

first_numbers_dataset = [10, 20, 30, 40, 50]
second_numbers_dataset = [30, 40, 50, 60, 70]

common_elements_list = []
for number_entry in first_numbers_dataset:
    if number_entry in second_numbers_dataset:
        common_elements_list.append(number_entry)

print("List 1:          " + str(first_numbers_dataset))
print("List 2:          " + str(second_numbers_dataset))
print("Common Elements: " + str(common_elements_list))
