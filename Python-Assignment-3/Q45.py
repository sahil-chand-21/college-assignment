# ASSIGNMENT 3 - QUESTION 45
# Program to demonstrate the use of append(), extend() and insert() methods.

working_items_list = [10, 20]
print("Initial List: " + str(working_items_list))

working_items_list.append(30)
print("After append(30):       " + str(working_items_list))

working_items_list.extend([40, 50])
print("After extend([40, 50]): " + str(working_items_list))

working_items_list.insert(1, 15)
print("After insert(1, 15):    " + str(working_items_list))
