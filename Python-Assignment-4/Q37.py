# ASSIGNMENT 4 - QUESTION 37
# Write a program to demonstrate the use of global variables inside a function.

global_institution_name = "Uttarakhand Technical University"

def print_institution_details():
    """Accesses a global variable from inside the function."""
    print("Inside function reading global variable: " + global_institution_name)

print_institution_details()
print("Outside function reading global variable: " + global_institution_name)
