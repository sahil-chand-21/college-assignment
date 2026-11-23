# ASSIGNMENT 3 - QUESTION 03
# Program to count vowels and consonants separately in a string.

input_text_sentence = "Computer Science Engineering"
vowels_collection = ['a', 'e', 'i', 'o', 'u']
vowels_counter = 0
consonants_counter = 0

for letter_character in input_text_sentence:
    if letter_character.isalpha():
        if letter_character.lower() in vowels_collection:
            vowels_counter += 1
        else:
            consonants_counter += 1

print("Sentence:          " + input_text_sentence)
print("Vowels Count:      " + str(vowels_counter))
print("Consonants Count:  " + str(consonants_counter))
