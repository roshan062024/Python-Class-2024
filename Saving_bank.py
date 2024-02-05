#!/usr/bin/python3
"""
Purpose: Saving Bank

    Initial Balance 0

Algorithm
----------
Step 1: Create an variable 'balance' with initial value 0
Step 2: Initial Despoit of min balance 1500
Step 3: Salary credited of 3300
Step 4: Online Purchase of 33.33
Step 5: House Rent paid of 1500
Step 6: Display Balance
"""


Balance = 0
Initial_Despoit = 1500
Salary_credited = 3300
Online_Purchase = 33.33
House_Rent = 1500

Balance = Initial_Despoit + Salary_credited - Online_Purchase - House_Rent

print(Balance)

