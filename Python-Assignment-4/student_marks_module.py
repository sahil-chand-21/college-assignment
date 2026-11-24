# User-defined module for Question 49
# Contains functions for student marks calculation.

def calculate_total_marks(marks_list):
    """Calculates and returns total marks from a list of marks."""
    total_score = sum(marks_list)
    return total_score

def calculate_percentage_score(marks_list, maximum_marks_per_subject=100):
    """Calculates and returns the percentage score."""
    total_score = sum(marks_list)
    maximum_possible_total = len(marks_list) * maximum_marks_per_subject
    percentage_result = (total_score / maximum_possible_total) * 100.0
    return percentage_result
