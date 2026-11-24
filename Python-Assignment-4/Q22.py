# ASSIGNMENT 4 - QUESTION 22
# Write a function to find the largest element in a list.

def find_largest_in_list(numbers_list):
    """Finds and returns the maximum element from a list."""
    if not numbers_list:
        return None
    current_largest_element = numbers_list[0]
    for list_element in numbers_list:
        if list_element > current_largest_element:
            current_largest_element = list_element
    return current_largest_element

dataset_numbers = [34, 78, 12, 95, 43, 67]
largest_element_result = find_largest_in_list(dataset_numbers)

print("List: " + str(dataset_numbers))
print("Largest Element: " + str(largest_element_result))
