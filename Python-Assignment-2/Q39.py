# ASSIGNMENT 2 - QUESTION 39
# Program to check whether a number is prime using a loop.

candidate_prime_number = 29
is_number_prime = True

if candidate_prime_number <= 1:
    is_number_prime = False
else:
    for divisor_candidate in range(2, int(candidate_prime_number ** 0.5) + 1):
        if candidate_prime_number % divisor_candidate == 0:
            is_number_prime = False
            break

print("Tested Number: " + str(candidate_prime_number))
if is_number_prime:
    print(str(candidate_prime_number) + " is a PRIME number.")
else:
    print(str(candidate_prime_number) + " is NOT a prime number.")
