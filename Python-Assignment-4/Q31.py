# ASSIGNMENT 4 - QUESTION 31
# Write a function to demonstrate default arguments.

def enroll_student_course(student_name, course_name="Python Programming", semester_number=1):
    """Demonstrates default arguments when optional parameters are omitted."""
    print("Student:  " + student_name)
    print("Course:   " + course_name)
    print("Semester: " + str(semester_number))
    print("---")

print("Call 1 (using all defaults):")
enroll_student_course("Rajat Verma")

print("Call 2 (overriding defaults):")
enroll_student_course("Deepa Sharma", course_name="Data Structures", semester_number=2)
