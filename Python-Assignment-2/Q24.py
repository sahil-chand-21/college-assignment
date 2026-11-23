# ASSIGNMENT 2 - QUESTION 24
# Program to find the greatest among three numbers.

first_number = 45
second_number = 89
third_number = 72

print("Numbers: " + str(first_number) + ", " + str(second_number) + ", " + str(third_number))

if (first_number >= second_number) and (first_number >= third_number):
    greatest_number = first_number
elif (second_number >= first_number) and (second_number >= third_number):
    greatest_number = second_number
else:
    greatest_number = third_number

print("The greatest among the three numbers is: " + str(greatest_number))
