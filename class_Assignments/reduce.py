# from functools import reduce

# def add(x, y):
#     if isinstance(y, (list, tuple)):
#         return x + custom_sum_reduce(y)
#     else:
#         return x + y

# def custom_sum_reduce(iterable, start=0):
#     return reduce(add, iterable, start)

# # Test cases
# print(custom_sum_reduce((1, 23, 23, 2)))
# print(custom_sum_reduce([(1, 2), (3), (9, 1)], ()))
# print(custom_sum_reduce([[1, 2], [3, 4]], []))
