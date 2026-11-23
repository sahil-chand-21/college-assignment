# ASSIGNMENT 3 - QUESTION 47
# Program to count the occurrences of a given element in a tuple using count().

roll_marks_tuple = (85, 90, 78, 85, 92, 85, 88)
searched_mark_value = 85

occurrences_count = roll_marks_tuple.count(searched_mark_value)

print("Marks Tuple: " + str(roll_marks_tuple))
print("Occurrences of " + str(searched_mark_value) + ": " + str(occurrences_count))
