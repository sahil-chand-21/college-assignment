# ASSIGNMENT 1 - QUESTION 45
# Program to accept the length and breadth of a rectangle and display its area.

length_input = input("Enter length of rectangle (default 12): ").strip()
rectangle_length = float(length_input) if length_input else 12.0

breadth_input = input("Enter breadth of rectangle (default 7): ").strip()
rectangle_breadth = float(breadth_input) if breadth_input else 7.0

calculated_rectangle_area = rectangle_length * rectangle_breadth

print("Length: " + str(rectangle_length) + ", Breadth: " + str(rectangle_breadth))
print("Area of Rectangle: " + str(calculated_rectangle_area))
