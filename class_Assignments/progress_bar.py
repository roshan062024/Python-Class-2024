
"""
Assignment: Progress bar implementation
    [          ]   3
    [*         ]  10
    [**        ]  20
    [***       ]  30
    [****      ]  40
    [*****     ]  50
    [******    ]  60
    [*******   ]  70
    [********  ]  80
    [********* ]  90
    [**********] 100
"""


data_set = range(-100, 10_00_000)
data_set_length = len(data_set)


for loop_index, _ in enumerate(data_set):
    # print(loop_index, loop_index / data_set_length)
    percent_completed = (loop_index / data_set_length) * 100
    percent_completed = round(percent_completed, 2)

    # print(percent_completed, end="\r")
    # print(f"{percent_completed:5} completed", end="\r")
    # print(f"\r{percent_completed:5} completed", end="")

    num_filled = int(percent_completed / 10)
    filled = '*' * num_filled
    print(f"\r[{filled:10}]{percent_completed:10} % Completed",end="")
    

