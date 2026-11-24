# ASSIGNMENT 4 - QUESTION 25
# Write a function to find the length of a string without using the len() function.

def calculate_string_length_without_len(input_string_data):
    """Counts and returns the length of a string without calling len()."""
    character_counter = 0
    for individual_character in input_string_data:
        character_counter += 1
    return character_counter

sample_text_sequence = "Problem Solving with Python"
counted_length_result = calculate_string_length_without_len(sample_text_sequence)

print("String: " + sample_text_sequence)
print("Length calculated manually: " + str(counted_length_result))
