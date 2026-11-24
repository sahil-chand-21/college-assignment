# ASSIGNMENT 4 - QUESTION 40
# Write a program to demonstrate how local variables behave when two different functions use variables with the same name.

def engineering_first_year_routine():
    classroom_identifier = "Room 101 - Lecture Hall"
    print("First Year Function:  " + classroom_identifier)

def engineering_final_year_routine():
    classroom_identifier = "Room 405 - Seminar Hall"
    print("Final Year Function:  " + classroom_identifier)

print("Demonstrating independent local variables in separate functions:")
engineering_first_year_routine()
engineering_final_year_routine()
