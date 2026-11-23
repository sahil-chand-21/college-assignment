# ASSIGNMENT 2 - QUESTION 30
# Program to calculate electricity charges using different slabs with nested if statements.

electricity_units_consumed = 240
calculated_electricity_bill = 0.0

print("Electricity Units Consumed: " + str(electricity_units_consumed))

if electricity_units_consumed <= 100:
    calculated_electricity_bill = electricity_units_consumed * 1.50
else:
    if electricity_units_consumed <= 200:
        calculated_electricity_bill = (100 * 1.50) + ((electricity_units_consumed - 100) * 2.50)
    else:
        if electricity_units_consumed <= 300:
            calculated_electricity_bill = (100 * 1.50) + (100 * 2.50) + ((electricity_units_consumed - 200) * 4.00)
        else:
            calculated_electricity_bill = (100 * 1.50) + (100 * 2.50) + (100 * 4.00) + ((electricity_units_consumed - 300) * 5.50)

print("Total Electricity Bill: Rs. " + str(calculated_electricity_bill))
