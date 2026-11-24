# ASSIGNMENT 4 - QUESTION 24
# Write a function to count vowels in a given string.

def count_vowels_in_string(target_sentence):
    """Counts vowels (a, e, i, o, u) in a string."""
    vowel_characters = ['a', 'e', 'i', 'o', 'u']
    detected_vowels_count = 0
    for single_character in target_sentence.lower():
        if single_character in vowel_characters:
            detected_vowels_count += 1
    return detected_vowels_count

sample_sentence_phrase = "Uttarakhand Technical University"
total_vowels_found = count_vowels_in_string(sample_sentence_phrase)

print("Sentence: " + sample_sentence_phrase)
print("Vowels Count: " + str(total_vowels_found))
