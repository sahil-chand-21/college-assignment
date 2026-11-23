# ASSIGNMENT 2 - QUESTION 44
# Program to print all pairs of numbers from 1 to 5 using nested loops.

print("All pairs of numbers from (1 to 5):")

for first_pair_element in range(1, 6):
    for second_pair_element in range(1, 6):
        print("(" + str(first_pair_element) + ", " + str(second_pair_element) + ")", end=" ")
    print()
