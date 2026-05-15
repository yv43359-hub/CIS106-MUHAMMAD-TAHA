players = []
averages = []

f = open("players.txt", "r")

for line in range(10):

    player = f.readline().rstrip("\n")
    avg = float(f.readline())

    players.append(player)
    averages.append(avg)

f.close()


def display(players, averages):

    for x in range(len(players)):
        print(players[x], averages[x])


def search(players, averages, name):

    for x in range(len(players)):

        if players[x] == name:
            print("Player:", players[x])
            print("Average:", averages[x])


display(players, averages)

choice = "YES"

while choice == "YES":

    lastname = input("Enter player last name: ")

    search(players, averages, lastname)

    choice = input("Do another? YES/NO: ").upper()