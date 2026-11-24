# ASSIGNMENT 4 - QUESTION 34
# Write a function that accepts a string and returns the number of uppercase and lowercase characters.

def count_uppercase_and_lowercase(input_prose_text):
    """Counts uppercase and lowercase characters in a string and returns both counts."""
    uppercase_letter_count = 0
    lowercase_letter_count = 0
    for scanned_character in input_prose_text:
        if scanned_character.isupper():
            uppercase_letter_count += 1
        elif scanned_character.islower():
            lowercase_letter_count += 1
    return uppercase_letter_count, lowercase_letter_count

sample_evaluated_phrase = "Hello World! Welcome to Python 2026"
upper_total, lower_total = count_uppercase_and_lowercase(sample_evaluated_phrase)

print("Evaluated Phrase: " + sample_evaluated_phrase)
print("Uppercase Characters Count: " + str(upper_total))
print("Lowercase Characters Count: " + str(lower_total))
