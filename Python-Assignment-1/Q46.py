# ASSIGNMENT 1 - QUESTION 46
# Program to accept five subject marks from the user and display their total.

print("Please provide marks for five subjects (leave empty to use default marks):")
subject_marks_list = []
default_marks = [75.0, 82.0, 91.0, 68.0, 85.0]

for subject_index in range(1, 6):
    user_prompt = "Enter marks for subject " + str(subject_index) + " (default " + str(default_marks[subject_index - 1]) + "): "
    entered_mark = input(user_prompt).strip()
    if entered_mark:
        subject_marks_list.append(float(entered_mark))
    else:
        subject_marks_list.append(default_marks[subject_index - 1])

total_marks_sum = sum(subject_marks_list)

print("Individual Subject Marks: " + str(subject_marks_list))
print("Total Calculated Marks:   " + str(total_marks_sum) + " out of 500")
