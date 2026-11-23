# ASSIGNMENT 2 - QUESTION 35
# Program to print the multiplication table of a given number.

multiplication_base_number = 7

print("Multiplication Table for " + str(multiplication_base_number) + ":")
for multiplier_factor in range(1, 11):
    table_product = multiplication_base_number * multiplier_factor
    print(str(multiplication_base_number) + " x " + str(multiplier_factor) + " = " + str(table_product))
