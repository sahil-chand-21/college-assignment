# ASSIGNMENT 1 - QUESTION 36
# Program to create a dictionary containing student details such as roll number, name and marks.

student_details_dictionary = {
    "roll_number": 230101,
    "student_name": "Priya Sharma",
    "subject_marks": {"Physics": 88, "Chemistry": 82, "Mathematics": 94}
}

print("Student Details Dictionary:")
for detail_key, detail_value in student_details_dictionary.items():
    print(str(detail_key) + ": " + str(detail_value))
