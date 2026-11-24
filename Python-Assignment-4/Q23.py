# ASSIGNMENT 4 - QUESTION 23
# Write a function to calculate the average of a list of numbers.

def calculate_list_average(numerical_values_list):
    """Calculates and returns the arithmetic average of numbers in a list."""
    if not numerical_values_list:
        return 0.0
    total_elements_sum = sum(numerical_values_list)
    total_elements_count = len(numerical_values_list)
    return total_elements_sum / total_elements_count

subject_scores_collection = [85, 90, 78, 92, 88]
computed_average_score = calculate_list_average(subject_scores_collection)

print("Scores List: " + str(subject_scores_collection))
print("Average Score: " + str(computed_average_score))
