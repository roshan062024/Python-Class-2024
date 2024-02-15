MAX_TABLE = 10

second = 0
while second < MAX_TABLE:  # O(n^2)
    second += 1
    first = 0
    while first < MAX_TABLE:
        first += 1
        print(f"{first} * {second} = {first * second:3} |",end=" ")
    print()
    
