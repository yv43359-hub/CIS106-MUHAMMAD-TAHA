players = []
averages = []

f = open("players.txt", "r")

for line in range(10):

    player = f.readline().rstrip("\n")
    avg = float(f.readline())

    players.append(player)
    averages.append(avg)

f.close()


def search(players, averages, name):

    found = False

    for x in range(len(players)):

        if players[x] == name:

            print("Player:", players[x])
            print("Average:", averages[x])

            found = True

    if found == False:
        print("Name not found")


choice = "YES"

while choice == "YES":

    lastname = input("Enter player last name: ")

    search(players, averages, lastname)

    choice = input("Do another? YES/NO: ").upper()