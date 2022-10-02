import random

EXP = 0
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
            print(f'You reached level {level}')
    return EXP, gained

while True:
    fight = str(input('Fight? '))

    if fight == 'yes':
        res = roll_exp(LEVELS)
        print(f'EXP Gained: {res[1]}')
        print(f'Total EXP: {res[0]}')
    else:
        quit()
