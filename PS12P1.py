# 1
numbers = []

count = int(input("How many numbers do you want to enter? "))

for x in range(count):

    num = int(input("Enter an integer: "))

    numbers.append(num)

print("List:", numbers)


# 2
numbers.insert(1, 99)

print("After inserting 99:", numbers)


# 3
index99 = numbers.index(99)

numbers[index99] = 100

print("After replacing 99 with 100:", numbers)


# 4
numbers2 = [500, 600, 700, 800, 900]

print("Second List:", numbers2)

numbers.extend(numbers2)

print("Extended First List:", numbers)


# 5
numbers.remove(800)

print("After removing 800:", numbers)


# 6
del numbers[2]

print("After removing third item:", numbers)


# 7
grades = ["A", "B", "C", "A", "A", "C"]


# 8
countA = grades.count("A")

print("Number of A grades:", countA)


# 9
indexB = grades.index("B")

print("Index of first B:", indexB)


# 10
if "F" in grades:
    print("F found")
else:
    print("F is not in the list")


# 11
numbers2.clear()

print("Cleared second list:", numbers2)


# 12
del numbers2

# print(numbers2)
# This would generate an error because the list no longer exists


# 13
players = ["Rizzo", "Davis", "Baez", "Happ", "Bryan"]

print("Players:", players)


# 14
players.sort()

print("Sorted Players:", players)


# 15
players2 = players.copy()

print("Players2:", players2)


# 16
players2.reverse()

print("Players:", players)

print("Players2 Reversed:", players2)