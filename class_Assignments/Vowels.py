#!/usr/bin/python3
"""
Purpose: To check whether the given character
        is vowels or consonant

        vowels - aeiou

in operator  works with any iterable object

Algorithms:
-------
step1 : take input in runtime
            clean -- strip()
Step2:  len(character) should not be greater than 1
step3: isalpha()
step4 : is it vowel or not

NOTE: logic should accomodate both upper and lower characters
"""


a = input("Enter the Character:")

vowels = "aeiouAEIOU"

if a.isalpha() == True and len(a) == 1:
    if a in vowels:
        print(f"{a} It's  a Vowel")
    else :
        print(f"{a} It's not a Vowel")
    


