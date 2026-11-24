# ASSIGNMENT 4 - QUESTION 21
# Write a function to calculate the sum of digits of a number.

def calculate_sum_of_digits(target_integer):
    """Calculates and returns the sum of digits of a given integer."""
    positive_number = abs(target_integer)
    digits_total_sum = 0
    while positive_number > 0:
        extracted_digit = positive_number % 10
        digits_total_sum += extracted_digit
        positive_number //= 10
    return digits_total_sum

sample_number_value = 5782
sum_result = calculate_sum_of_digits(sample_number_value)

print("Sample Number: " + str(sample_number_value))
print("Sum of Digits: " + str(sum_result))
