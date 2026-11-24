# ASSIGNMENT 4 - QUESTION 18
# Write a function to check whether a number is prime.

def is_prime_number(evaluated_number):
    """Returns True if the number is prime, False otherwise."""
    if evaluated_number <= 1:
        return False
    for divisor_candidate in range(2, int(evaluated_number ** 0.5) + 1):
        if evaluated_number % divisor_candidate == 0:
            return False
    return True

tested_number_entry = 31

print("Tested Number: " + str(tested_number_entry))
if is_prime_number(tested_number_entry):
    print(str(tested_number_entry) + " is a PRIME number.")
else:
    print(str(tested_number_entry) + " is NOT a prime number.")
