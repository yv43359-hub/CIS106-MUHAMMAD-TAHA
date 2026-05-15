total = 0
tax = 0


def compute_total(qty, unit_price):

    global total
    global tax

    total = qty * unit_price

    tax = total * 0.07


qty = float(input("Enter quantity: "))

unit_price = float(input("Enter unit price: "))

compute_total(qty, unit_price)

print("Total: $", format(total, ".2f"))
print("Tax: $", format(tax, ".2f"))