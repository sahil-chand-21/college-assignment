# ASSIGNMENT 2 - QUESTION 34
# Program to calculate the factorial of a given number using a loop.

target_factorial_number = 6
computed_factorial_result = 1

for multiplication_factor in range(1, target_factorial_number + 1):
    computed_factorial_result *= multiplication_factor

print("Given Number: " + str(target_factorial_number))
print("Factorial (" + str(target_factorial_number) + "!): " + str(computed_factorial_result))
