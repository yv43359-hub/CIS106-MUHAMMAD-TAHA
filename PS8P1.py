def compute_total(qty, price):
  total = qty * price

  if total > 10000:
      total = total * 0.90

  return total


choice = "Y"
grand_total = 0

while choice == "Y":

  qty = float(input("Enter quantity: "))
  price = float(input("Enter price: "))
total = compute_total(qty, price)
grand_total = grand_total + total
print("Quantity:", qty)
print("Price:", price)
print("Total: $", format(total, ".2f"))
choice = input("Do another? (Y/N): ").upper()
print("Grand Total: $", format(grand_total, ".2f"))
