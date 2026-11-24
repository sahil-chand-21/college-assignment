# ASSIGNMENT 4 - QUESTION 17
# Write a function to calculate the factorial of a number.

def compute_factorial_using_loop(target_number):
    """Computes factorial of a given non-negative integer using a loop."""
    if target_number < 0:
        return "Factorial undefined for negative numbers"
    accumulated_factorial = 1
    for current_multiplier in range(1, target_number + 1):
        accumulated_factorial *= current_multiplier
    return accumulated_factorial

evaluated_number = 6
factorial_output = compute_factorial_using_loop(evaluated_number)

print("Given Number: " + str(evaluated_number))
print("Factorial: " + str(factorial_output))
