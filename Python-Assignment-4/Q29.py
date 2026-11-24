# ASSIGNMENT 4 - QUESTION 29
# Write a function to demonstrate positional arguments.

def display_student_marks_report(student_name, roll_number, percentage_score):
    """Demonstrates positional arguments: arguments are matched by position."""
    print("Student Name:     " + student_name)
    print("Roll Number:      " + str(roll_number))
    print("Percentage Score: " + str(percentage_score) + "%")

# Arguments passed strictly in position order: student_name, roll_number, percentage_score
print("Calling function using positional arguments:")
display_student_marks_report("Neha Bisht", 230401, 89.5)
