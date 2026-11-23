# ASSIGNMENT 2 - QUESTION 42
# Program to print the following number pattern using nested loops:
# 1
# 12
# 123
# 1234
# 12345

number_pattern_row_count = 5

for current_level in range(1, number_pattern_row_count + 1):
    for column_number in range(1, current_level + 1):
        print(str(column_number), end="")
    print()
