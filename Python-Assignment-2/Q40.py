# ASSIGNMENT 2 - QUESTION 40
# Program to print all prime numbers within a given range.

range_start_boundary = 10
range_end_boundary = 50

print("Prime numbers between " + str(range_start_boundary) + " and " + str(range_end_boundary) + ":")

for candidate_number in range(range_start_boundary, range_end_boundary + 1):
    if candidate_number > 1:
        is_candidate_prime = True
        for trial_divisor in range(2, int(candidate_number ** 0.5) + 1):
            if candidate_number % trial_divisor == 0:
                is_candidate_prime = False
                break
        if is_candidate_prime:
            print(str(candidate_number), end=" ")
print()
