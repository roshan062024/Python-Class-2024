input1 = input( "enter word :")

rev_input = input1[::-1]

print("Word :{0} \nRev_word : {1}".format(input1,rev_input) )

if input1 == rev_input :
    print("True")
else:
    print("false")