def compute_forecast(month, sales):

    if month in ["JAN", "FEB", "MAR"]:
        percent = 0.10

    elif month in ["APR", "MAY", "JUN"]:
        percent = 0.15

    elif month in ["JUL", "AUG", "SEP"]:
        percent = 0.20

    else:
        percent = 0.25

    forecast_sales = sales * (1 + percent)

    return forecast_sales


choice = "YES"

while choice == "YES":

    lastname = input("Enter last name: ")
    month = input("Enter month: ").upper()
    sales = float(input("Enter sales: "))

    forecast = compute_forecast(month, sales)

    print("Last Name:", lastname)
    print("Forecast Sales: $", format(forecast, ".2f"))

    choice = input("Do another? (YES/NO): ").upper()