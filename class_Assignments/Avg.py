"""
Purpose: Calculating the average for the
    inputted numbers in run-time
"""
lst = []
 
n = int(input("Enter number of elements : "))
 
i = 0
while i < n:
    ele = int(input())
    lst.append(ele)
    i += 1

a = tuple(lst)

Avg = sum(a)/len(a)
print(f"Avg of given numbers is : {Avg}")

