# ASSIGNMENT 4 - QUESTION 49
# Write a program to create a user-defined module for student marks calculation
# and use it in another Python program.

import student_marks_module

student_obtained_marks = [78, 85, 92, 69, 88]

calculated_total = student_marks_module.calculate_total_marks(student_obtained_marks)
calculated_percentage = student_marks_module.calculate_percentage_score(student_obtained_marks)

print("Imported student_marks_module successfully.")
print("Subject Marks: " + str(student_obtained_marks))
print("Total Marks using module: " + str(calculated_total) + " / 500")
print("Percentage Score using module: " + str(round(calculated_percentage, 2)) + "%")
