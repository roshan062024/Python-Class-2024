
from functools import reduce

numbers = input("Enter numbers separated by space: ").split()
numbers = list(map(int, numbers))  

result = reduce(lambda x, y: x + y, numbers)
print(result)



