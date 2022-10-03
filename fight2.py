import random

EXP = 0
LEVELS = [0, 10, 20, 35, 50, 75, 100, 140, 200]

def roll_exp():
    global EXP
    global LEVELS
    gained = random.randint(4, 8)
    EXP = gained + EXP
    for level in LEVELS:
        if EXP <= level:
            return LEVELS.index(level), gained, EXP

while True:
    fight = str(input('Fight? '))

    if fight == 'yes':
        res = roll_exp()
        print(res)
        print(f'Current level: {res[0]}')
        print(f'EXP Gained: {res[1]}')
        print(f'Total EXP: {res[2]}')
    else:
        quit()
