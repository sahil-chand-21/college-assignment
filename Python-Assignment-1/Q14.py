# ASSIGNMENT 1 - QUESTION 14
# Program to calculate simple interest using principal, rate and time.

principal_amount = 10000.0
annual_interest_rate = 6.5
time_duration_years = 3.0

calculated_simple_interest = (principal_amount * annual_interest_rate * time_duration_years) / 100.0
total_maturity_amount = principal_amount + calculated_simple_interest

print("Principal Amount:    Rs.", principal_amount)
print("Interest Rate:       ", annual_interest_rate, "%")
print("Time Period:         ", time_duration_years, "years")
print("Simple Interest:     Rs.", calculated_simple_interest)
print("Total Amount:        Rs.", total_maturity_amount)
