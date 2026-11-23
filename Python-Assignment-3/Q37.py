# ASSIGNMENT 3 - QUESTION 37
# Program to find the second-largest element in a list.

numbers_data_sample = [45, 88, 12, 88, 76, 92, 34]

# Remove duplicates by converting to set, then sort
unique_numbers_sorted = sorted(list(set(numbers_data_sample)))

if len(unique_numbers_sorted) >= 2:
    second_largest_number = unique_numbers_sorted[-2]
    print("List:                   " + str(numbers_data_sample))
    print("Second Largest Element: " + str(second_largest_number))
else:
    print("List does not contain enough unique elements.")
