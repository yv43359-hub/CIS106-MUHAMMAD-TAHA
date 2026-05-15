names = ["Smith", "Jones", "Adams", "Clark", "Brown",
   "White", "Hall", "Green", "Young", "King"]


def display_names(arr):

for x in arr:
  print(x)


def reverse_names(arr):

for x in range(len(arr)-1, -1, -1):
  print(arr[x])


print("Names")
display_names(names)

print("\nReverse Order")
reverse_names(names)