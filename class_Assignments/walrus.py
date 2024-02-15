numbers = [2, 8, 0, 1, 1, 9, 7, 7]
description = {
    "length": (
        num_length := len(numbers)
    ),  # Here we are initializing and using both at the same time
    "sum": (num_sum := sum(numbers)),
    "mean": num_sum / num_length,
}
print(description)  # {'length': 8, 'sum': 35, 'mean': 4.375}