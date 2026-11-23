# ASSIGNMENT 2 - QUESTION 33
# Program to calculate the sum of the first N natural numbers.

natural_numbers_limit = 20
accumulated_natural_sum = 0

for natural_counter in range(1, natural_numbers_limit + 1):
    accumulated_natural_sum += natural_counter

print("Upper Limit (N): " + str(natural_numbers_limit))
print("Sum of first " + str(natural_numbers_limit) + " natural numbers: " + str(accumulated_natural_sum))
