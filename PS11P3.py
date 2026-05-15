names = []
scores = []

f = open("scores.txt", "r")

for line in range(10):

    name = f.readline().rstrip("\n")
    score = float(f.readline())

    names.append(name)
    scores.append(score)

f.close()


def high_low(names, scores):

    high_var = 0
    low_var = 999

    for x in range(len(scores)):

        if scores[x] > high_var:
            high_var = scores[x]
            high_index = x

        if scores[x] < low_var:
            low_var = scores[x]
            low_index = x

    print("Highest:", names[high_index], high_var)
    print("Lowest:", names[low_index], low_var)


high_low(names, scores)