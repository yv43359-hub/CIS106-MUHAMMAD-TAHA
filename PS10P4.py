def compute_average(score1, score2, score3, handicap):

    average = (score1 + score2 + score3) / 3

    average_with_handicap = average + handicap

    return average, average_with_handicap


lastname = input("Enter bowler last name: ")

score1 = float(input("Enter game 1 score: "))
score2 = float(input("Enter game 2 score: "))
score3 = float(input("Enter game 3 score: "))

handicap = float(input("Enter handicap: "))

avg, handicap_avg = compute_average(score1, score2, score3, handicap)

print("Bowler:", lastname)
print("Average Score:", format(avg, ".2f"))
print("Average With Handicap:", format(handicap_avg, ".2f"))