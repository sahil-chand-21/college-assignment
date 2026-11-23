# ASSIGNMENT 1 - QUESTION 48
# Program to demonstrate the use of print() with multiple variables and formatted output.

student_full_name = "Anjali Negi"
student_roll_number = 23045
student_marks_percentage = 94.678

# Using multiple variables with separators
print("Student Details:", student_full_name, student_roll_number, student_marks_percentage, sep=" | ")

# Using string concatenation with +
print("Concatenation with +: Roll No. " + str(student_roll_number) + " (" + student_full_name + ") secured " + str(round(student_marks_percentage, 2)) + "%")

# Using str.format() method
print("Format Method: Name: {0}, Roll: {1}, Percentage: {2:.1f}%".format(student_full_name, student_roll_number, student_marks_percentage))
