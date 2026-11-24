# ASSIGNMENT 4 - QUESTION 28
# Write a function to calculate simple interest using arguments and a return statement.

def calculate_simple_interest(principal_amount, annual_rate, duration_years):
    """Calculates and returns simple interest based on principal, rate, and time."""
    computed_interest = (principal_amount * annual_rate * duration_years) / 100.0
    return computed_interest

borrowed_principal = 25000.0
interest_rate_percent = 7.5
loan_time_years = 4.0

interest_amount_result = calculate_simple_interest(borrowed_principal, interest_rate_percent, loan_time_years)

print("Principal: Rs. " + str(borrowed_principal))
print("Rate: " + str(interest_rate_percent) + "%")
print("Time: " + str(loan_time_years) + " years")
print("Simple Interest: Rs. " + str(interest_amount_result))
