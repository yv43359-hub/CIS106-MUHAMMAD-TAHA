f = open("items.txt", "r")

total_extended = 0
count = 0

item = f.readline().rstrip("\n")

while item != "":

    quantity = float(f.readline())
    price = float(f.readline())

    extended = quantity * price

    total_extended = total_extended + extended
    count = count + 1

    print("Item:", item)
    print("Quantity:", quantity)
    print("Price: $", format(price, ".2f"))
    print("Extended Price: $", format(extended, ".2f"))
    print()
    item = f.readline().rstrip("\n")

    average = total_extended / count

    print("Total Extended Prices: $", format(total_extended, ".2f"))
    print("Number of Orders:", count)
    print("Average Order: $", format(average, ".2f"))

    f.close()