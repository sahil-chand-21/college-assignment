# ASSIGNMENT 4 - QUESTION 09
# Program to calculate the value of sine, cosine and tangent for a given angle.
import math

angle_in_degrees = 45.0
angle_in_radians = math.radians(angle_in_degrees)

calculated_sine_value = math.sin(angle_in_radians)
calculated_cosine_value = math.cos(angle_in_radians)
calculated_tangent_value = math.tan(angle_in_radians)

print("Angle in Degrees: " + str(angle_in_degrees))
print("Sine Value:    " + str(round(calculated_sine_value, 4)))
print("Cosine Value:  " + str(round(calculated_cosine_value, 4)))
print("Tangent Value: " + str(round(calculated_tangent_value, 4)))
