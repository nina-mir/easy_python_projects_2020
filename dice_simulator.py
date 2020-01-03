# taking 1 input parameter (number of dices; max.10) from the user
# code roles the dice(s)
# dice values are from 1 to 6

import random

print("enter the number of dices you wish to roll [maximum 10 dices]")

num_dices = int(input("how many dices? [wie viele Würfel?]"))


def roll_the_dice(num_dices):
    list = []
    for _ in range(num_dices):
        list.append(random.randrange(1, 6, 1))
    print(list)


roll_the_dice(num_dices)
