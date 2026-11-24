# ASSIGNMENT 4 - QUESTION 47
# Write a program to use the random module to generate five random integers.
import random

print("Generating five random integers between 10 and 100 using random.randint():")
random_integers_list = []

for random_index in range(1, 6):
    generated_random_value = random.randint(10, 100)
    random_integers_list.append(generated_random_value)
    print("Random Integer " + str(random_index) + ": " + str(generated_random_value))

print("Collected List: " + str(random_integers_list))
