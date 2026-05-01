symbol = input("Enter stock symbol: ")
shares = int(input("Enter number of shares: "))
price = float(input("Enter cost per share: "))

total = shares * price

print("Stock:", symbol)
print("Total investment:", total)