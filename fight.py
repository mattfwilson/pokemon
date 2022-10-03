import random

EXP = 15
LEVELS = {
    1:10,
    2:20,
    3:35,
    4:50,
    5:75,
    6:100,
    7:140
    }


def roll_exp(levels):
    global EXP
    gained = random.randint(4, 8)
    EXP = gained + EXP
    for level in levels:
        if levels[level] <= EXP:
            print(level)
    return gained, EXP

while True:
    fight = str(input('Fight? '))

    if fight == 'yes':
        res = roll_exp(LEVELS)
        print(res)
        print(f'EXP Gained: {res[0]}')
        print(f'Total EXP: {res[1]}')
    else:
        quit()
