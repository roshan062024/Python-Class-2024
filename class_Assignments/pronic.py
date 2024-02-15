for i in range(1, 11):
    for j in range(1, 11):
        if i+1 == j or i == j-1:
            print(f"{i} * {j} = {i * j}")
        
