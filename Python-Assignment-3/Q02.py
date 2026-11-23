# ASSIGNMENT 3 - QUESTION 02
# Program to count the number of vowels in a given string.

sample_text_phrase = "Programming in Python is Fun and Powerful"
vowels_reference_list = ['a', 'e', 'i', 'o', 'u']
total_vowels_count = 0

for current_character in sample_text_phrase:
    if current_character.lower() in vowels_reference_list:
        total_vowels_count += 1

print("Given Phrase:  " + sample_text_phrase)
print("Vowels Count:  " + str(total_vowels_count))
