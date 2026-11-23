# ASSIGNMENT 2 - QUESTION 47
# Program to demonstrate the use of the pass statement inside a loop.

print("Demonstrating pass statement inside loop:")

for element_index in range(1, 6):
    if element_index == 3:
        # Pass acts as a placeholder for future implementation
        pass
        print("Number 3 encountered: executed pass statement")
    else:
        print("Processing element: " + str(element_index))
