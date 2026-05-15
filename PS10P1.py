def compute_discount(qty, price, rate):

    total = qty * price

    discount_amount = total * rate

    discounted_price = total - discount_amount

    return discount_amount, discounted_price


qty = float(input("Enter quantity: "))
price = float(input("Enter price: "))
rate = float(input("Enter discount rate: "))

discount, final_price = compute_discount(qty, price, rate)

print("Quantity:", qty)
print("Price: $", format(price, ".2f"))
print("Discount Amount: $", format(discount, ".2f"))
print("Discounted Price: $", format(final_price, ".2f"))