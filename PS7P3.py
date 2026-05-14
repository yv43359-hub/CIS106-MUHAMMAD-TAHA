f = open("employees.txt", "r")

total_bonus = 0

name = f.readline().rstrip("\n")

while name != "":

    salary = float(f.readline())

    if salary >= 100000:
        rate = 0.20
    elif salary >= 50000:
        rate = 0.15
    else:
        rate = 0.10

    bonus = salary * rate

    total_bonus = total_bonus + bonus

    print("Employee:", name)
    print("Salary: $", format(salary, ".2f"))
    print("Bonus: $", format(bonus, ".2f"))
    print()

        name = f.readline().rstrip("\n")

    print("Total Bonuses Paid: $", format(total_bonus, ".2f"))

    f.close()