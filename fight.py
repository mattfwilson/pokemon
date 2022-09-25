import random

exp = 0

levels = {
    1:10,
    2: 20,
    3:35,
    4:50,
    5:75
    }

def roll_exp(current_exp):
    gained = random.randint(4, 8)
    total = gained + current_exp
    return total, gained

while True:

    fight = str(input('Fight? '))

    if fight == 'yes':
        res = roll_exp(exp)
        print(f'Gained: {res[1]}')
        print(f'Current exp: {res[0]}')
    else:
        quit()
