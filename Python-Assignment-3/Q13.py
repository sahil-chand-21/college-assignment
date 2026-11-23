# ASSIGNMENT 3 - QUESTION 13
# Program to check whether a given string starts and ends with a particular character.

examined_filename = "_configuration_backup_"
prefix_check_character = "_"
suffix_check_character = "_"

starts_with_character = examined_filename.startswith(prefix_check_character)
ends_with_character = examined_filename.endswith(suffix_check_character)

print("Filename:     " + examined_filename)
print("Starts with '" + prefix_check_character + "': " + str(starts_with_character))
print("Ends with '" + suffix_check_character + "':   " + str(ends_with_character))
