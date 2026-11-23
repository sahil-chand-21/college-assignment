# ASSIGNMENT 2 - QUESTION 50
# Program to print the following pattern using nested loops:
# *****
# ****
# ***
# **
# *

maximum_row_stars = 5

for row_star_count in range(maximum_row_stars, 0, -1):
    for star_symbol_index in range(1, row_star_count + 1):
        print("*", end="")
    print()
