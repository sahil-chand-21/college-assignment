# ASSIGNMENT 3 - QUESTION 33
# Program to delete an element from a list using the remove() method.

registered_colors = ["Red", "Green", "Blue", "Yellow", "Orange"]
color_to_remove = "Blue"

print("Before Removal: " + str(registered_colors))
registered_colors.remove(color_to_remove)
print("After Removing '" + color_to_remove + "': " + str(registered_colors))
