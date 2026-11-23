# ASSIGNMENT 3 - QUESTION 20
# Program to demonstrate string formatting using the format() method and string concatenation (+).

student_first_name = "Kavita"
student_roll_no = 104
student_aggregate_score = 91.5

# Demonstration using str.format()
formatted_by_method = "Student Name: {0}, Roll: {1}, Score: {2:.1f}%".format(student_first_name, student_roll_no, student_aggregate_score)

# Demonstration using string concatenation (+)
formatted_by_concatenation = "Student Name: " + student_first_name + ", Roll: " + str(student_roll_no) + ", Score: " + str(student_aggregate_score) + "%"

print("Using format() method:       " + formatted_by_method)
print("Using concatenation with +:  " + formatted_by_concatenation)
