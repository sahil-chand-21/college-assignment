# ASSIGNMENT 4 - QUESTION 33
# Write a function that accepts a list as an argument and returns its largest element.

def retrieve_max_element_from_list(incoming_numbers_list):
    """Accepts a list as an argument and returns the maximum element."""
    if not incoming_numbers_list:
        return None
    maximum_found_number = incoming_numbers_list[0]
    for current_number_item in incoming_numbers_list:
        if current_number_item > maximum_found_number:
            maximum_found_number = current_number_item
    return maximum_found_number

sample_integers_sequence = [19, 45, 82, 33, 91, 24]
highest_result_element = retrieve_max_element_from_list(sample_integers_sequence)

print("Incoming List: " + str(sample_integers_sequence))
print("Largest Element: " + str(highest_result_element))
