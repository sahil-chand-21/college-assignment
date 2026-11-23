# ASSIGNMENT 1 - QUESTION 33
# Program to create a list containing different data types.

heterogeneous_student_record = ["Aman Singh", 102, 8.85, True, ["Maths", "Python"]]

print("List containing different data types:")
print(heterogeneous_student_record)
for item_element in heterogeneous_student_record:
    print("Element: " + str(item_element) + " | Type: " + str(type(item_element)))
