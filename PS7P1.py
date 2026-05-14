principal = float(input("Enter principal amount: "))
rate = float(input("Enter interest rate: "))

total_interest = 0

print("Year\tBeginning Balance\tEnding Balance")

for year in range(1, 6):

    beginning = principal
    interest = principal * rate
    ending = principal + interest

    total_interest = total_interest + interest

    print(year, "\t$", format(beginning, ".2f"),
          "\t\t$", format(ending, ".2f"))

    principal = ending

print("Total interest earned: $", format(total_interest, ".2f"))