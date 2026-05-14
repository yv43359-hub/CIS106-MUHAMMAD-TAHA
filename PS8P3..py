def mpg(miles, gallons):
  result = miles / gallons
  return result


choice = "Y"
count = 0

while choice == "Y":

  city = input("Enter destination city: ")
  miles = float(input("Enter miles traveled: "))
  gallons = float(input("Enter gallons used: "))

  result = mpg(miles, gallons)

  count = count + 1

  print("City:", city)
  print("Miles:", miles)
  print("MPG:", format(result, ".2f"))

  choice = input("Do another? (Y/N): ").upper()

print("Number of trips entered:", count)