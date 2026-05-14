f = open("students.txt", "r")

total_tuition = 0
count = 0

name = f.readline().rstrip("\n")

while name != "":

    district = f.readline().rstrip("\n")
    credits = float(f.readline())

    if district == "I":
        cost = 250
    else:
        cost = 500

    tuition = credits * cost
    total_tuition = total_tuition + tuition
        count = count + 1

        print("Student:", name)
        print("Credits:", credits)
        print("Tuition Owed: $", format(tuition, ".2f"))
        print()

        name = f.readline().rstrip("\n")

    print("Total Tuition Owed: $", format(total_tuition, ".2f"))
    print("Number of Students:", count)

    f.close()