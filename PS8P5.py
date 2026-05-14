def tuition(credits, district):

    if district == "I":
        total = credits * 250
    else:
        total = credits * 550

    return total


choice = "Y"
total_tuition = 0

while choice == "Y":

    name = input("Enter student last name: ")
    credits = float(input("Enter credit hours: "))
    district = input("Enter district code (I/O): ").upper()

    amount = tuition(credits, district)

    total_tuition = total_tuition + amount

    print("Student:", name)
    print("Tuition Owed: $", format(amount, ".2f"))

    choice = input("Do another? (Y/N): ").upper()

print("Total Tuition Owed: $", format(total_tuition, ".2f"))