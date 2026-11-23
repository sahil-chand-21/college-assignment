# ASSIGNMENT 2 - QUESTION 20
# Program to evaluate expressions and demonstrate Python operator precedence.

expression_result_default = 10 + 20 * 2 ** 3 / 4 - 5
expression_result_grouped = (10 + 20) * (2 ** (3 / 4)) - 5

print("Expression 1: 10 + 20 * 2 ** 3 / 4 - 5")
print("Precedence Order: Exponentiation (**) -> Mult/Div (*, /) -> Add/Sub (+, -)")
print("Result: " + str(expression_result_default))

print("\nExpression 2 with explicit parentheses: (10 + 20) * (2 ** (3 / 4)) - 5")
print("Result: " + str(expression_result_grouped))
