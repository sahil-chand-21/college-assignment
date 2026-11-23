# ASSIGNMENT 2 - QUESTION 48
# Program to demonstrate the else clause of a for loop.

search_key_value = 25
sample_numbers_collection = [10, 20, 30, 40, 50]

print("Collection: " + str(sample_numbers_collection))
print("Searching for: " + str(search_key_value))

for current_item in sample_numbers_collection:
    if current_item == search_key_value:
        print("Found key in collection.")
        break
else:
    print("Loop finished without finding the key (else branch executed).")
