# ASSIGNMENT 3 - QUESTION 12
# Program to find the first and last occurrence of a character using string methods.

source_corpus_text = "dehradun educational department"
searched_letter = "d"

first_index_position = source_corpus_text.find(searched_letter)
last_index_position = source_corpus_text.rfind(searched_letter)

print("Corpus Text:      " + source_corpus_text)
print("Target Letter:    " + searched_letter)
print("First Occurrence: Index " + str(first_index_position))
print("Last Occurrence:  Index " + str(last_index_position))
