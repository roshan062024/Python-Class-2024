'''
# Assignment
# -------------
# caesar cipher
# ------------------  + 3
# A B C D E F G H I J     Y Z
# 0 1 2 3 4 5 6 7
# D E F


# Ex: egg => hjj
#    bindu => elqg
#    Yash  => bd..

# ASSUMPTION: Ignore case -sensitivity
# HINTS: ord(), chr(), % 
'''

Input_Text = input("Enter the Word : ").lower()
# print(Input_Text)
shift = int(input("enter shift :"))
output = []

for i in list(Input_Text):

    shifted_char = chr(((ord(i) - 97 + shift) % 26) + 97)
    output.append(shifted_char)
out_put = "".join(output)
print(f"Cipher Code : {out_put}")
    