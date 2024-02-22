"""Assignment
----------
1) write a function to mimick the sum() function.
    Caution: don't create function with same name

2) write a function to implement the following:
    - input: ((1,2), 3,4, [5, 6])
    - output: (1, 2, 3, 4, 5, 6)

    HINT: isinstance() - builtin function
          int(), float(), list(), tuple(), set()
          list.append(), list.extend
          list & tuple concatenation
"""

def sum_add(*nums):
    sum = 0
    for i in nums:
        sum = i + sum
    return sum


add = sum_add(10,20,30)
print(f"SUM : {add}")

add = sum_add(10,20)
print(f"SUM : {add}")


add = sum_add(10,20,30,40,50,60,70)
print(f"SUM : {add}")





def tup(input):
    a=[]
    for i in input:
        if isinstance(i,tuple) == True:
            for j in i:
                a.append(j)
        if isinstance(i,list) == True:
            for j in i:
                a.append(j)
        if isinstance(i,int) == True:
            a.append(i)
    return tuple(a)


input = ((1,2), 3,4, [5, 6])

x=tup(input)
print(x)