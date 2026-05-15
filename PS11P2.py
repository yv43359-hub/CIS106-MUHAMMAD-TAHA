names = ["Smith", "Jones", "Adams", "Clark", "Brown",
   "White", "Hall", "Green", "Young", "King"]

scores = [88, 91, 75, 84, 93, 79, 85, 90, 87, 95]


def display_arrays(names, scores):

for x in range(len(names)):
  print(names[x], scores[x])


def reverse_arrays(names, scores):

for x in range(len(names)-1, -1, -1):
  print(names[x], scores[x])


print("Students and Scores")
display_arrays(names, scores)

print("\nReverse Order")
reverse_arrays(names, scores)