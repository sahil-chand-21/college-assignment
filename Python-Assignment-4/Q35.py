# ASSIGNMENT 4 - QUESTION 35
# Write a function that returns both the sum and product of two numbers.

def compute_sum_and_product(first_operand, second_operand):
    """Calculates and returns both the sum and product of two numbers."""
    calculated_sum_val = first_operand + second_operand
    calculated_product_val = first_operand * second_operand
    return calculated_sum_val, calculated_product_val

number_alpha = 12
number_beta = 5
sum_result_val, product_result_val = compute_sum_and_product(number_alpha, number_beta)

print("First Number: " + str(number_alpha))
print("Second Number: " + str(number_beta))
print("Calculated Sum: " + str(sum_result_val))
print("Calculated Product: " + str(product_result_val))
