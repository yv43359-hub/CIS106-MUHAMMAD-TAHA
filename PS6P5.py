response = input("Do you want to continue? Yes or No: ")

totaldiscount = 0

while response == "Yes":

    qty = float(input("Enter quantity: "))
    price = float(input("Enter price: "))

    extendedprice = qty * price

    if extendedprice > 10000:
        discount = extendedprice * 0.25
    else:
        discount = extendedprice * 0.10

    total = extendedprice - discount

    print("Extended Price:", extendedprice)
    print("Discount Amount:", discount)
    print("Total:", total)

    totaldiscount = totaldiscount + discount

    response = input("Do you want to continue? Yes or No: ")

    print("Sum of all discounts:", totaldiscount)