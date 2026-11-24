# ASSIGNMENT 4 - QUESTION 36
# Write a program to demonstrate the use of local variables inside a function.

def demonstrate_local_scope():
    """Function demonstrating that local variables are accessible only within this function."""
    local_student_score = 95
    local_student_name = "Abhishek"
    print("Inside function: Student Name: " + local_student_name)
    print("Inside function: Student Score: " + str(local_student_score))

demonstrate_local_scope()

# Attempting to access local_student_score here would raise NameError
print("Outside function: Local variables are not accessible in global scope.")
