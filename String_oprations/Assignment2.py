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
words = Input_Text.split()
# print(Input_Text)
shift = int(input("enter shift :"))

out_sentence =[]
for word in words:
    output = []
    for i in list(word):

        shifted_char = chr(((ord(i) - 97 + shift) % 26) + 97)
        output.append(shifted_char)
        out_put = "".join(output)
    out_sentence.append(out_put)    
cipher = " ".join(out_sentence)
print(f"Cipher Code : {cipher}")
    