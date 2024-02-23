"""
Assignments
------------
1) Develop a calculator software which does +, -, *, / operations
    Then, make use of partial functions to optimize your solution.
"""

import functools

def add_var(a,b):
    print(a+b)

def sub_var(a,b):
    print(a-b)

def mul_var(a,b):
    print(a*b)

def div_var(a,b):
    print(a/b)



def cal(opt,x,y):
    if opt == 1:
        return add_var(a,b)


    if opt == 2:
        return sub_var(a,b)
        
    if opt == 3:
        return mul_var(a,b)
       
    if opt == 4:
        return div_var(a,b)
        


a = int(input("enter the numbers :"))
b = int(input("enter the numbers :"))

opt = int(input("Select option : 1)add 2)sub 3)multi 4)div \n"))
ad = functools.partial(cal,opt)
ad(a,b)




