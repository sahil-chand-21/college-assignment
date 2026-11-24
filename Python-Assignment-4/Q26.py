# ASSIGNMENT 4 - QUESTION 26
# Write a function that accepts two arguments and returns their product.

def compute_product_of_two(first_multiplier, second_multiplier):
    """Accepts two arguments and returns their multiplication product."""
    multiplication_result = first_multiplier * second_multiplier
    return multiplication_result

multiplication_factor_one = 14
multiplication_factor_two = 8
returned_product_value = compute_product_of_two(multiplication_factor_one, multiplication_factor_two)

print("First Number: " + str(multiplication_factor_one))
print("Second Number: " + str(multiplication_factor_two))
print("Product: " + str(returned_product_value))
