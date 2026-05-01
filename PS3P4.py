# Auto discount calculator

make = input("Enter car make: ")
model = input("Enter car model: ")
msrp = float(input("Enter MSRP amount: "))
discount = float(input("Enter discount percent (decimal, e.g. 0.10): "))

amount_off = msrp * discount
discounted_price = msrp - amount_off

print("\nCar Details:")
print("Make:", make)
print("Model:", model)
print("MSRP:", msrp)
print("Discount percent:", discount)
print("Amount off:", amount_off)
print("Discounted price:", discounted_price)