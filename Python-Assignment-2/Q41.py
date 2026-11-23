# ASSIGNMENT 2 - QUESTION 41
# Program to print the following pattern using nested loops:
# *
# **
# ***
# ****
# *****

total_pattern_rows = 5

for current_row_index in range(1, total_pattern_rows + 1):
    for star_counter in range(1, current_row_index + 1):
        print("*", end="")
    print()
