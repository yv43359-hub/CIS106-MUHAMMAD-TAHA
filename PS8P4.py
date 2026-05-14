def pay_rate(code):

    if code == "L":
        return 25

    elif code == "A":
        return 30

    else:
        return 50


choice = "Y"
total_gross = 0

while choice == "Y":

    name = input("Enter employee last name: ")
    code = input("Enter job code (L/A/J): ").upper()
    hours = float(input("Enter hours worked: "))

    rate = pay_rate(code)

    if hours > 40:
        gross = (40 * rate) + ((hours - 40) * rate * 1.5)
    else:
        gross = hours * rate

    total_gross = total_gross + gross

    print("Employee:", name)
    print("Gross Pay: $", format(gross, ".2f"))

    choice = input("Do another? (Y/N): ").upper()

print("Total Gross Pay: $", format(total_gross, ".2f"))