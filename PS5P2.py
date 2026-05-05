item = input("Enter part number: ")
qty = int(input("Enter quantity: "))

if item == "10" or item == "55":
    cost = 1
elif item == "99":
    cost = 2
elif item == "80" or item == "70":
    cost = 3
else:
    cost = 5

total = qty * cost

print("Part Number:", item)
print("Unit Cost:", cost)
print("Total Cost:", total)