MAX_TABLE = 10

first = 1
while first < MAX_TABLE:  # O(n^2)

    second = 0
    while second < MAX_TABLE:
        second += 1
        print(f"{first:2} * {second:2} = {first * second:3} |",end=" ")
    print()
    first += 1
