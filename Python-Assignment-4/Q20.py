# ASSIGNMENT 4 - QUESTION 20
# Write a function to reverse a given string.

def reverse_string_manually(source_string):
    """Reverses and returns a string without using built-in reverse function."""
    reversed_accumulator = ""
    for character_element in source_string:
        reversed_accumulator = character_element + reversed_accumulator
    return reversed_accumulator

sample_text_word = "University"
reversed_word_output = reverse_string_manually(sample_text_word)

print("Original String: " + sample_text_word)
print("Reversed String: " + reversed_word_output)
