# ASSIGNMENT 3 - QUESTION 27
# Program to access the first, last and middle elements of a list.

sample_elements_list = [101, 202, 303, 404, 505, 606, 707]

first_list_element = sample_elements_list[0]
last_list_element = sample_elements_list[-1]
middle_list_index = len(sample_elements_list) // 2
middle_list_element = sample_elements_list[middle_list_index]

print("List:           " + str(sample_elements_list))
print("First Element:  " + str(first_list_element))
print("Middle Element: " + str(middle_list_element))
print("Last Element:   " + str(last_list_element))
