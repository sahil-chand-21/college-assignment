# ASSIGNMENT 3 - QUESTION 18
# Program to find the longest word in a given sentence using string operations.

input_prose_sentence = "Artificial intelligence revolutionizes engineering computation"
tokens_collection = input_prose_sentence.split()

longest_detected_word = ""
for current_token in tokens_collection:
    if len(current_token) > len(longest_detected_word):
        longest_detected_word = current_token

print("Sentence:     " + input_prose_sentence)
print("Longest Word: " + longest_detected_word + " (Length: " + str(len(longest_detected_word)) + ")")
