# ASSIGNMENT 3 - QUESTION 32
# Program to append five elements to an existing list.

students_roster = ["Rohan", "Sneha"]
new_joining_students = ["Kiran", "Meera", "Deepak", "Pooja", "Vikram"]

print("Original Roster: " + str(students_roster))

for incoming_student in new_joining_students:
    students_roster.append(incoming_student)

print("Updated Roster after appending 5 elements:")
print(students_roster)
