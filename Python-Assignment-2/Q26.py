# ASSIGNMENT 2 - QUESTION 26
# Program to check whether a person is eligible to vote.

candidate_voter_age = 19
LEGAL_VOTING_AGE_LIMIT = 18

print("Candidate Age: " + str(candidate_voter_age))
if candidate_voter_age >= LEGAL_VOTING_AGE_LIMIT:
    print("Eligible to vote in elections.")
else:
    print("Not eligible to vote. Minimum age is " + str(LEGAL_VOTING_AGE_LIMIT) + ".")
