# Three doors, one contains the wealth, other two contains nothing
# Pick one door, another nothing door opens
# Test the winning rate if keeping the choice

# The following is a test for random choosing winning rate
# doors = [0, 1, 2]
# count = 0
# num = 1000
#
# for i in range(0, num):
#     random.shuffle(doors)
#     # print(doors)
#
#     if doors[0] == 0:
#         count += 1
#
# print(count/num)

# randomly choose a door
# another nothing door is picked
# change the door and record if winning
# check the winning rate


import random


def randie(n):
    return random.randint(0, n)


num = 100000
index_num = 3
doors = list(range(index_num))
count = 0

for i in range(num):
    random.shuffle(doors)  # create random doors
    print(doors)
    first_choice = randie(index_num-1)  # make choice
    # print(choice)
    nothing_one = int
    while True:  # pick nothing door
        nothing_one = randie(index_num-1)

        if nothing_one != first_choice and doors[nothing_one] != 0:
            break
    # print(nothing_one)

    choices = list(range(index_num))
    choices.remove(first_choice)
    choices.remove(nothing_one)
    # pick the third door
    final_choice = choices[0]
    if doors[final_choice] == 0:
        count += 1

print(count/num)
