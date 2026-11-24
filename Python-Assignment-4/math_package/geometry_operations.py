# Module 2 in math_package
# Contains geometric calculation functions.
import math

def compute_circle_area(radius_length):
    return math.pi * (radius_length ** 2)

def compute_rectangle_perimeter(length_dimension, breadth_dimension):
    return 2 * (length_dimension + breadth_dimension)
