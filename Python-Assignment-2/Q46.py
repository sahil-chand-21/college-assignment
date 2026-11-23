# ASSIGNMENT 2 - QUESTION 46
# Program to print numbers from 1 to 20 while skipping multiples of 3 using continue.

print("Numbers from 1 to 20 skipping multiples of 3:")

for sequential_number in range(1, 21):
    if sequential_number % 3 == 0:
        continue
    print(str(sequential_number), end=" ")
print()
