# ASSIGNMENT 4 - QUESTION 30
# Write a function to demonstrate keyword arguments.

def describe_faculty_member(faculty_name, department_name, years_experience):
    """Demonstrates keyword arguments: passed by parameter name, order does not matter."""
    print("Faculty:    " + faculty_name)
    print("Department: " + department_name)
    print("Experience: " + str(years_experience) + " years")

# Arguments passed using explicit parameter keywords in varied order
print("Calling function using keyword arguments:")
describe_faculty_member(department_name="Computer Science", years_experience=12, faculty_name="Dr. S. K. Joshi")
