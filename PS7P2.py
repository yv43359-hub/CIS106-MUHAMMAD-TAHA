first = 1
second = 1

print(first)
print(second)

for count in range(18):

    next_num = first + second

    print(next_num)

    first = second
    second = next_num