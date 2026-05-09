response = input("Do you want to continue? Yes or No: ")

count = 0
totalgross = 0

while response == "Yes":

    lname = input("Enter employee last name: ")
    hours = float(input("Enter hours worked: "))
    rate = float(input("Enter rate of pay: "))

    if hours > 40:
        grosspay = (40 * rate) + ((hours - 40) * rate * 1.5)
    else:
        grosspay = hours * rate

    print("Last Name:", lname)
    print("Gross Pay:", grosspay)

    totalgross = totalgross + grosspay
    count = count + 1
    response = input("Do you want to continue? Yes or No: ")

    averagepay = totalgross / count

    print("Total Gross Pay:", totalgross)
    print("Number of Employees:", count)
    print("Average Pay:", averagepay)