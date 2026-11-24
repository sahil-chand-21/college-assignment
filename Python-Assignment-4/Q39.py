# ASSIGNMENT 4 - QUESTION 39
# Write a program to modify a global variable inside a function using the global keyword.

enrolled_students_counter = 50

def admit_new_students(additional_students_count):
    """Modifies the global variable using the global keyword."""
    global enrolled_students_counter
    enrolled_students_counter += additional_students_count
    print("Inside function: Enrolled count updated to: " + str(enrolled_students_counter))

print("Before function call: " + str(enrolled_students_counter))
admit_new_students(15)
print("After function call (Globally Modified): " + str(enrolled_students_counter))
