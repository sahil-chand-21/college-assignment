# ASSIGNMENT 3 - QUESTION 06
# Program to count uppercase and lowercase characters in a string.

sample_mixed_string = "Welcome to UTU Python Assignment 2026"
uppercase_letters_count = 0
lowercase_letters_count = 0

for inspected_character in sample_mixed_string:
    if inspected_character.isupper():
        uppercase_letters_count += 1
    elif inspected_character.islower():
        lowercase_letters_count += 1

print("Sample String:    " + sample_mixed_string)
print("Uppercase Count:  " + str(uppercase_letters_count))
print("Lowercase Count:  " + str(lowercase_letters_count))
