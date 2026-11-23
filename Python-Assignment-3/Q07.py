# ASSIGNMENT 3 - QUESTION 07
# Program to count the number of digits, alphabets and special characters in a string.

analysed_text_string = "Roll_No: 230101, Grade: A+!"
alphabets_tally = 0
digits_tally = 0
special_characters_tally = 0

for scanned_char in analysed_text_string:
    if scanned_char.isalpha():
        alphabets_tally += 1
    elif scanned_char.isdigit():
        digits_tally += 1
    elif not scanned_char.isspace():
        special_characters_tally += 1

print("String:              " + analysed_text_string)
print("Alphabets Count:     " + str(alphabets_tally))
print("Digits Count:        " + str(digits_tally))
print("Special Chars Count: " + str(special_characters_tally))
