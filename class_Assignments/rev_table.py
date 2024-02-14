MAX_TABLE = 10

first = MAX_TABLE
while first > 0:  # O(n^2)
    
    second = MAX_TABLE+1
    while second > 0:
        second -= 1
        print(f"{first:2} * {second:2} = {first * second:3}")
    first -= 1
    print("\n")
    
    