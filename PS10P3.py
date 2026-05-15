def compute_sales(sales):

    if sales > 100000:
        commission = sales * 0.10
    else:
        commission = sales * 0.05

    next_target = sales * 1.05

    return commission, next_target


lastname = input("Enter salesperson last name: ")

sales = float(input("Enter sales amount: "))

commission, target = compute_sales(sales)

print("Salesperson:", lastname)
print("Commission: $", format(commission, ".2f"))
print("Next Year Target: $", format(target, ".2f"))