def compute_assessed(county, market_value):

    if county == "COOK":
        percent = 0.90

    elif county == "DUPAGE":
        percent = 0.80

    elif county == "MCHENRY":
        percent = 0.75

    elif county == "KANE":
        percent = 0.60

    else:
        percent = 0.70

    assessed = market_value * percent

    return assessed


choice = "YES"

total_market = 0
total_assessed = 0

while choice == "YES":

    county = input("Enter county: ").upper()
    market_value = float(input("Enter market value: "))

    assessed = compute_assessed(county, market_value)

    total_market = total_market + market_value
    total_assessed = total_assessed + assessed

    print("County:", county)
    print("Assessed Value: $", format(assessed, ".2f"))

    choice = input("Do another? (YES/NO): ").upper()

print("Total Market Value: $", format(total_market, ".2f"))
print("Total Assessed Value: $", format(total_assessed, ".2f"))