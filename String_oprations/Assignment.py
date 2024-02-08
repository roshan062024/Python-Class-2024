'''
 Assignment: reverse each word in given sentence in same order
 input : today is good day
 output: yadot si doog yad
'''

Text = input("Enter the text :")
rev_words =[]

input = Text.split()
for input in input :
    rev_word = input[::-1]
    rev_words.append(rev_word)


rev_output = ' '.join(rev_words)

# string reversal

print("output : ", rev_output)