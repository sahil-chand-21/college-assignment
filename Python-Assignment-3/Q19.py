# ASSIGNMENT 3 - QUESTION 19
# Program to count the frequency of each character in a string.

target_phrase_string = "engineering"
characters_frequency_map = {}

for character_symbol in target_phrase_string:
    if character_symbol in characters_frequency_map:
        characters_frequency_map[character_symbol] += 1
    else:
        characters_frequency_map[character_symbol] = 1

print("String: " + target_phrase_string)
print("Character Frequencies:")
for mapped_char, char_frequency in characters_frequency_map.items():
    print("'" + mapped_char + "' : " + str(char_frequency))
