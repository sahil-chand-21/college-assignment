# ASSIGNMENT 1 - QUESTION 43
# Program to demonstrate the use of input() to accept a student's name and display a welcome message.

entered_student_name = input("Enter your name: ").strip()
if not entered_student_name:
    entered_student_name = "Student"

print("Hearty Welcome, " + entered_student_name + "! Glad to have you in the Python Course.")
