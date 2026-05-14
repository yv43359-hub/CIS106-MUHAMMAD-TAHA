def compute_price(msrp, make, model, electric):

    if electric == "Y":
        percent = 0.30

    elif make == "HONDA" and model == "ACCORD":
        percent = 0.10

    elif make == "TOYOTA" and model == "RAV4":
        percent = 0.15

    else:
        percent = 0.05

    discount = msrp * percent

    new_price = msrp - discount

    tax = new_price * 0.07

    total = new_price + tax

    return total


choice = "YES"

total_msrp = 0
total_sales = 0

while choice == "YES":

    make = input("Enter make: ").upper()
    model = input("Enter model: ").upper()
    electric = input("Electric vehicle (Y/N): ").upper()
    msrp = float(input("Enter MSRP: "))

    total = compute_price(msrp, make, model, electric)

    total_msrp = total_msrp + msrp
    total_sales = total_sales + total

    print("Sales Price: $", format(total, ".2f"))

    choice = input("Do another? (YES/NO): ").upper()

print("Total MSRP: $", format(total_msrp, ".2f"))
print("Total Sales Price: $", format(total_sales, ".2f"))