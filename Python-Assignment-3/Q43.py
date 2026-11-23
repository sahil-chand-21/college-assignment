# ASSIGNMENT 3 - QUESTION 43
# Program to find the index of a specified element in a list.

frameworks_list = ["Django", "Flask", "FastAPI", "Pyramid"]
search_framework = "FastAPI"

detected_index = frameworks_list.index(search_framework)

print("Frameworks: " + str(frameworks_list))
print("Index of '" + search_framework + "': " + str(detected_index))
