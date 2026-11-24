# ASSIGNMENT 4 - QUESTION 38
# Write a program to demonstrate the difference between local and global variables having the same name.

course_name_identifier = "Master in Technology (Global)"

def sample_academic_function():
    course_name_identifier = "Bachelor in Technology (Local)"
    print("Inside function (Local Shadowing): " + course_name_identifier)

sample_academic_function()
print("Outside function (Global Intact): " + course_name_identifier)
