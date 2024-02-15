#!/usr/bin/python3
"""
Purpose: Number Guessing Game

    break - To come out of any loop (for/while)
    Assignment
    ------------------------
    attempts        points
    -----------------------
    1-3             100
    4-9              60
    10-16            20
    17-25             5
    26-               0
"""
LUCKY_NUMBER = 67
MAX_ATTEMPTS = 100

# Method 5 - Giving Infinite Attempts; but tracking attempts
attempt = 0
while True:  # do-while loop 
    attempt += 1
    print(f'\n{attempt = }')

    given_number = int(input('Enter no. between 0 & 100:'))
    if given_number == LUCKY_NUMBER:
        print('You guessed correctly!')
        if attempt in range(1,3):
            print("your Score is : 100")
        elif attempt in range(4,9):
            print("your Score is : 60")
        elif attempt in range(10,16):
            print("your Score is : 20")
        elif attempt in range(17,25):
            print("your Score is : 5")
        elif attempt in range(26,100):
            print("your Score is : 0")
        break

    elif given_number > LUCKY_NUMBER:  # 87 > 67
        print('Reduce your guessing number')
    else:  # given_number < LUCKY_NUMBER
        print('Increase your guessing number')
# else:  # CODE IS NOT REACHABLE
#     print("It will never reach here, as loop breaks to exit")



"""