# ASSIGNMENT 3 - QUESTION 05
# Program to check whether a given string is a palindrome.

candidate_palindrome_word = "Radar"
normalized_word = candidate_palindrome_word.lower()

# Check palindrome by slicing
is_palindrome_match = (normalized_word == normalized_word[::-1])

print("Candidate Word: " + candidate_palindrome_word)
if is_palindrome_match:
    print("The word '" + candidate_palindrome_word + "' is a PALINDROME.")
else:
    print("The word '" + candidate_palindrome_word + "' is NOT a palindrome.")
