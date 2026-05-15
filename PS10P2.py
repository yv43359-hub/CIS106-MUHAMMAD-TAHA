def compute_scores(score1, score2, score3):

    total = score1 + score2 + score3

    average = total / 3

    return total, average


lastname = input("Enter student last name: ")

score1 = float(input("Enter exam 1 score: "))
score2 = float(input("Enter exam 2 score: "))
score3 = float(input("Enter exam 3 score: "))

total_points, average_score = compute_scores(score1, score2, score3)

print("Student:", lastname)
print("Total Points:", format(total_points, ".2f"))
print("Average Score:", format(average_score, ".2f"))