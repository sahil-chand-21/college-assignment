# ASSIGNMENT 2 - QUESTION 45
# Program to demonstrate the use of the break statement in a loop.

target_search_number = 7
print("Searching for number " + str(target_search_number) + " in range 1 to 15:")

for iteration_number in range(1, 16):
    print("Checking number: " + str(iteration_number))
    if iteration_number == target_search_number:
        print("Target number " + str(target_search_number) + " found! Terminating loop with break.")
        break
