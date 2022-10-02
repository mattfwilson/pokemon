import random

exp = 0

levels = {
    1:10,
    2:20,
    3:35,
    4:50,
    5:75
    }

def roll_exp():
    global exp
    gained = random.randint(4, 8)
    exp = gained + exp
    return exp, gained

while True:

    fight = str(input('Fight? '))

    if fight == 'yes':
        res = roll_exp()
        print(f'EXP Gained: {res[1]}')
        print(f'Total EXP: {res[0]}')
    else:
        quit()
