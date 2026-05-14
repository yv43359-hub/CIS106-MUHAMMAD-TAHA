def batting_average(hits, at_bats):
  avg = hits / at_bats
  return avg


choice = "Y"
count = 0

while choice == "Y":

  name = input("Enter player last name: ")
  hits = int(input("Enter hits: "))
  at_bats = int(input("Enter at bats: "))

  avg = batting_average(hits, at_bats)

  count = count + 1

  print("Player:", name)
  print("Batting Average:", format(avg, ".3f"))

  choice = input("Do another? (Y/N): ").upper()

print("Number of players entered:", count)