# ASSIGNMENT 1 - QUESTION 47
# Program to demonstrate the use of list(), tuple() and dict() constructors.

source_sequence = "PYTHON"

constructed_list = list(source_sequence)
constructed_tuple = tuple(source_sequence)
constructed_dictionary = dict([("lang", "Python"), ("version", 3)])

print("Constructed with list(): ", constructed_list, type(constructed_list))
print("Constructed with tuple():", constructed_tuple, type(constructed_tuple))
print("Constructed with dict(): ", constructed_dictionary, type(constructed_dictionary))
