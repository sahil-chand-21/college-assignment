# ASSIGNMENT 3 - QUESTION 34
# Program to delete an element from a specified index using pop().

course_topics_list = ["Basics", "Conditions", "Loops", "Obsolete Topic", "Functions"]
index_to_pop = 3

print("Before Pop: " + str(course_topics_list))
removed_topic_element = course_topics_list.pop(index_to_pop)
print("Popped Element: " + str(removed_topic_element))
print("After Pop:      " + str(course_topics_list))
