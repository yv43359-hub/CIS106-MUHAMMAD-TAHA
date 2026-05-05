principal = float(input("Enter principal amount: "))
years = int(input("Enter years to maturity: "))

if principal > 100000 and years == 5:
    rate = 0.06
elif principal >= 50000 and principal <= 100000 and years == 10:
    rate = 0.05
elif principal >= 50000 and principal <= 100000 and years == 5:
    rate = 0.04
else:
    rate = 0.02

interest = principal * rate

print("Principal:", principal)
print("Interest Rate:", rate)
print("Interest Amount:", interest)