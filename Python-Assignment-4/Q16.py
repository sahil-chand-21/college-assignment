# ASSIGNMENT 4 - QUESTION 16
# Write a function to find the greatest among three numbers.

def find_greatest_of_three(first_value, second_value, third_value):
    """Determines the greatest of three values."""
    if (first_value >= second_value) and (first_value >= third_value):
        return first_value
    elif (second_value >= first_value) and (second_value >= third_value):
        return second_value
    else:
        return third_value

number_one = 45
number_two = 87
number_three = 63

greatest_result = find_greatest_of_three(number_one, number_two, number_three)
print("Given Numbers: " + str(number_one) + ", " + str(number_two) + ", " + str(number_three))
print("The Greatest Number is: " + str(greatest_result))
