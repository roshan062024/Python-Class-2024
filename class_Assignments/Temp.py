#!/usr/bin/python3
"""
Purpose: Temperature Conversions
    - celsius to fahrenheit


farhenheit = (1.8 * celsius) + 32  # PEMDAS

Algorithm:
step 1: take celcius , clear and validate 
step 2: convert and give farhenheit
"""

a = input("Enter the Temperature :").strip()
temp = float(a[:-1])
unit = a[-1]
# print(unit)
# print(temp)
if unit.lower() == "c" :
 farhenheit = (1.8 * temp) + 32
 print(f"Temp is {round(farhenheit,2)} F")
elif unit.lower() == "f":
 cel = (temp - 32) * 5/9 
 print(f" Temp is {round(cel,2)} C")
else :
 print("Not a Temp ")



