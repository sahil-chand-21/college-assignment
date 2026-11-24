# ASSIGNMENT 4 - QUESTION 19
# Write a function to check whether a string is a palindrome.

def check_palindrome_string(input_text_string):
    """Checks whether the given string reads the same forwards and backwards."""
    cleaned_string = input_text_string.lower().replace(" ", "")
    return cleaned_string == cleaned_string[::-1]

test_word_one = "Madam"
test_word_two = "Python"

print("Is '" + test_word_one + "' palindrome? " + str(check_palindrome_string(test_word_one)))
print("Is '" + test_word_two + "' palindrome? " + str(check_palindrome_string(test_word_two)))
