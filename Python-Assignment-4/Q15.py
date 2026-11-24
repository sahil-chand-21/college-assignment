# ASSIGNMENT 4 - QUESTION 15
# Write a function to check whether a number is even or odd.

def check_even_or_odd(tested_number):
    """Checks whether a number is even or odd."""
    if tested_number % 2 == 0:
        return "EVEN"
    else:
        return "ODD"

candidate_number_one = 28
candidate_number_two = 35

print("Number " + str(candidate_number_one) + " is: " + check_even_or_odd(candidate_number_one))
print("Number " + str(candidate_number_two) + " is: " + check_even_or_odd(candidate_number_two))
