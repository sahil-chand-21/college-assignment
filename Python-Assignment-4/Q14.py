# ASSIGNMENT 4 - QUESTION 14
# Write a function to find the square and cube of a given number.

def find_square_and_cube(given_number):
    """Calculates square and cube of a given number and returns both."""
    number_squared = given_number ** 2
    number_cubed = given_number ** 3
    return number_squared, number_cubed

selected_number = 5
squared_value, cubed_value = find_square_and_cube(selected_number)

print("Selected Number: " + str(selected_number))
print("Square: " + str(squared_value))
print("Cube: " + str(cubed_value))
