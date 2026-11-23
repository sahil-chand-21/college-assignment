# ASSIGNMENT 2 - QUESTION 49
# Program to demonstrate the else clause of a while loop.

countdown_step = 5

print("Starting while loop countdown:")
while countdown_step > 0:
    print("Count: " + str(countdown_step))
    countdown_step -= 1
else:
    print("Countdown finished normally! Executed while-else clause.")
