# ASSIGNMENT 2 - QUESTION 12
# Program to demonstrate AND, OR and NOT logical operators.

condition_student_passed = True
condition_fees_cleared = False

logical_and_result = condition_student_passed and condition_fees_cleared
logical_or_result = condition_student_passed or condition_fees_cleared
logical_not_result = not condition_student_passed

print("Condition Passed: " + str(condition_student_passed) + ", Condition Fees Cleared: " + str(condition_fees_cleared))
print("AND Result:       " + str(logical_and_result))
print("OR Result:        " + str(logical_or_result))
print("NOT Result:       " + str(logical_not_result))
