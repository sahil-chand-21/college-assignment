# ASSIGNMENT 1 - QUESTION 40
# Program to demonstrate the use of Boolean variables.

is_exam_cleared = True
has_pending_attendance_shortage = False

print("Exam Cleared Status:       ", is_exam_cleared)
print("Attendance Shortage Status:", has_pending_attendance_shortage)
print("Eligible for Promotion:    ", is_exam_cleared and not has_pending_attendance_shortage)
