# ASSIGNMENT 3 - QUESTION 35
# Program to sort a list in ascending and descending order.

unsorted_scores_list = [64, 34, 25, 12, 22, 11, 90]

ascending_sorted_list = sorted(unsorted_scores_list)
descending_sorted_list = sorted(unsorted_scores_list, reverse=True)

print("Original List:   " + str(unsorted_scores_list))
print("Ascending Order:  " + str(ascending_sorted_list))
print("Descending Order: " + str(descending_sorted_list))
