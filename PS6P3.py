response = input("Do you want to continue? Yes or No: ")

count = 0

while response == "Yes":

    lname = input("Enter last name: ")
    exam1 = float(input("Enter exam 1 score: "))
    exam2 = float(input("Enter exam 2 score: "))

    average = (exam1 + exam2) / 2

    print("Last Name:", lname)
    print("Average:", average)

    count = count + 1

    response = input("Do you want to continue? Yes or No: ")

print("Number of students entered:", count)