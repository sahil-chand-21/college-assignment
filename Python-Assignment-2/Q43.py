# ASSIGNMENT 2 - QUESTION 43
# Program to print a multiplication table from 1 to 10 using nested loops.

print("Multiplication Tables from 1 to 10:\n")

for outer_table_number in range(1, 11):
    print("--- Table for " + str(outer_table_number) + " ---")
    for inner_multiplier in range(1, 11):
        multiplied_value = outer_table_number * inner_multiplier
        print(str(outer_table_number) + " x " + str(inner_multiplier) + " = " + str(multiplied_value))
    print()
