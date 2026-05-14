def compute_square_feet(length, width, height):

    sqft = (2 * length * width) + (2 * length * height) + (2 * width * height)

    return sqft


choice = "YES"

while choice == "YES":

    length = float(input("Enter length: "))
    width = float(input("Enter width: "))
    height = float(input("Enter height: "))

    sqft = compute_square_feet(length, width, height)

    gallons = sqft / 50

    print("Square Footage:", format(sqft, ".2f"))
    print("Gallons Needed:", format(gallons, ".2f"))

    choice = input("Do another? (YES/NO): ").upper()