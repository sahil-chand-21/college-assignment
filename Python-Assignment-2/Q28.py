# ASSIGNMENT 2 - QUESTION 28
# Program to check whether a character is a vowel or consonant.

input_alphabet_character = "E"
normalized_character = input_alphabet_character.lower()

print("Given Character: " + input_alphabet_character)

if normalized_character.isalpha():
    if normalized_character in ['a', 'e', 'i', 'o', 'u']:
        print("The character '" + input_alphabet_character + "' is a VOWEL.")
    else:
        print("The character '" + input_alphabet_character + "' is a CONSONANT.")
else:
    print("The given input is not an alphabetical character.")
