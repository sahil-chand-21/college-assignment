# ASSIGNMENT 4 - QUESTION 32
# Write a function to demonstrate variable-length arguments using *args.

def calculate_aggregate_total(*subject_scores):
    """Accepts arbitrary number of positional arguments using *args."""
    total_aggregate = sum(subject_scores)
    total_subjects_count = len(subject_scores)
    print("Subject Scores: " + str(subject_scores))
    print("Total Subjects: " + str(total_subjects_count))
    print("Aggregate Total: " + str(total_aggregate))
    print("---")

print("Demonstrating *args:")
calculate_aggregate_total(75, 80, 85)
calculate_aggregate_total(90, 85, 95, 78, 88)
