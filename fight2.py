import random

EXP = 0
LEVELS = [0, 10, 20, 35, 50, 75, 100, 140, 200]
ACTIONS = ['Rock', 'Scissors', 'Paper']

def roll_exp():
    global EXP
    global LEVELS
    gained = random.randint(4, 8)
    EXP = gained + EXP
    for level in LEVELS:
        if EXP <= level:
            return LEVELS.index(level), gained, EXP

def check_outcome(player_choice):
    global ACTIONS
    
    p_choice = ACTIONS.index(player_choice)
    print(f'{p_choice} - Player chose {player_choice}.')

    comp_choice = random.choice(ACTIONS)
    c_choice = ACTIONS.index(comp_choice)
    print(f'{c_choice} - Computer chose {comp_choice}.')

    if c_choice + 1 % 3 == p_choice:
        print(f'You lose!')
    elif p_choice + 1 % 3 == c_choice:
        print(f'You win!')
    else:
        print(f'Tie.')

while True:
    action = str(input('Fight? '))
    check_outcome(action)

    # if action == 'rock':
    #     pass
    # elif action == 'paper':
    #     pass
    # elif action == 'scissors':
    #     pass
    # else:
    #     quit()

    # if fight == 'yes':
    #     result = roll_exp()
    #     print(result)
    #     print(f'Current level: {result[0]}')
    #     print(f'EXP Gained: {result[1]}')
    #     print(f'Total EXP: {result[2]}')
    # else:
    #     quit()
