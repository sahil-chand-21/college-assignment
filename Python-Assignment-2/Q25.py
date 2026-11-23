# ASSIGNMENT 2 - QUESTION 25
# Program to check whether a given year is a leap year.

inspected_calendar_year = 2024

is_leap_year = (inspected_calendar_year % 4 == 0 and inspected_calendar_year % 100 != 0) or (inspected_calendar_year % 400 == 0)

print("Year: " + str(inspected_calendar_year))
if is_leap_year:
    print(str(inspected_calendar_year) + " is a LEAP YEAR.")
else:
    print(str(inspected_calendar_year) + " is NOT a leap year.")
