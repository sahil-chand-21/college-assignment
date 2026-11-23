# ASSIGNMENT 1 - QUESTION 42
# Program to demonstrate the use of the id() function for different variables.

primary_identifier_number = 100
secondary_identifier_number = 100
distinct_identifier_number = 200

print("Memory ID of primary_identifier_number:  ", id(primary_identifier_number))
print("Memory ID of secondary_identifier_number:", id(secondary_identifier_number))
print("Memory ID of distinct_identifier_number: ", id(distinct_identifier_number))
print("Do primary and secondary point to same memory location?", id(primary_identifier_number) == id(secondary_identifier_number))
