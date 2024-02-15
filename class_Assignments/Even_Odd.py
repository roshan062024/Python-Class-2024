#!/usr/bin/python3
"""
Purpose: Check even-ness of a given number, in runtime.
"""

a = int(input("Enter the starting number :"))
b = int(input("Enter the Last number :"))
c =[]
for i in range(a):
    if i % 2 == 0:
        c.append(str(i))

d = ','.join(c)

print(f"Even Number's {d}")
       

