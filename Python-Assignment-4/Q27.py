# ASSIGNMENT 4 - QUESTION 27
# Write a function that accepts three numbers and returns the greatest number.

def get_greatest_among_three(number_entry_one, number_entry_two, number_entry_three):
    """Returns the greatest of three input numbers."""
    if (number_entry_one >= number_entry_two) and (number_entry_one >= number_entry_three):
        return number_entry_one
    elif (number_entry_two >= number_entry_one) and (number_entry_two >= number_entry_three):
        return number_entry_two
    else:
        return number_entry_three

first_test_val = 56
second_test_val = 94
third_test_val = 71

greatest_returned_number = get_greatest_among_three(first_test_val, second_test_val, third_test_val)

print("Numbers: " + str(first_test_val) + ", " + str(second_test_val) + ", " + str(third_test_val))
print("Greatest Number: " + str(greatest_returned_number))
