qty = int(input("Enter quantity: "))

if qty > 10000:
    price = 10
elif qty >= 5000:
    price = 20
else:
    price = 30

extended = qty * price
tax = extended * 0.07
total = extended + tax

print("Quantity:", qty)
print("Unit Price:", price)
print("Extended Price:", extended)
print("Tax:", tax)
print("Total:", total)