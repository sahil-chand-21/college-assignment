# ASSIGNMENT 2 - QUESTION 27
# Program to assign grades based on student marks using if-elif-else.

obtained_score_percentage = 82.5

print("Student Score: " + str(obtained_score_percentage) + "%")

if obtained_score_percentage >= 90.0:
    assigned_grade = "A+ (Outstanding)"
elif obtained_score_percentage >= 80.0:
    assigned_grade = "A (Excellent)"
elif obtained_score_percentage >= 70.0:
    assigned_grade = "B (Good)"
elif obtained_score_percentage >= 60.0:
    assigned_grade = "C (Satisfactory)"
elif obtained_score_percentage >= 50.0:
    assigned_grade = "D (Pass)"
else:
    assigned_grade = "F (Fail)"

print("Assigned Grade: " + assigned_grade)
