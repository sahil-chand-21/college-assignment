# ASSIGNMENT 3 - QUESTION 30
# Program to count the number of even and odd elements in a list.

integer_collection = [11, 24, 33, 48, 55, 62, 77, 86, 99]
even_numbers_count = 0
odd_numbers_count = 0

for current_integer in integer_collection:
    if current_integer % 2 == 0:
        even_numbers_count += 1
    else:
        odd_numbers_count += 1

print("Integer Collection: " + str(integer_collection))
print("Even Numbers Count: " + str(even_numbers_count))
print("Odd Numbers Count:  " + str(odd_numbers_count))
