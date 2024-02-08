'''
 Assignment: reverse each word in given sentence in same order
 input : today is good day
 output: yadot si doog yad
'''

Text = input("Enter the text :")

input = Text.split()
rev_input = [input[::-1] for input in input]

rev_output = ' '.join(rev_input)

# string reversal

print("output : ", rev_output)