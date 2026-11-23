# ASSIGNMENT 2 - QUESTION 37
# Program to count the number of digits in a given integer.

target_integer_number = 987654
temporary_digit_counter_number = target_integer_number
counted_digits_total = 0

if temporary_digit_counter_number == 0:
    counted_digits_total = 1
else:
    while temporary_digit_counter_number > 0:
        counted_digits_total += 1
        temporary_digit_counter_number //= 10

print("Number:          " + str(target_integer_number))
print("Number of Digits:" + str(counted_digits_total))
