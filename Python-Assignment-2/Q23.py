# ASSIGNMENT 2 - QUESTION 23
# Program to find the greatest among two numbers.

first_comparison_value = 84
second_comparison_value = 67

print("First Number:  " + str(first_comparison_value))
print("Second Number: " + str(second_comparison_value))

if first_comparison_value > second_comparison_value:
    print("The greatest number is: " + str(first_comparison_value))
elif second_comparison_value > first_comparison_value:
    print("The greatest number is: " + str(second_comparison_value))
else:
    print("Both numbers are equal.")
