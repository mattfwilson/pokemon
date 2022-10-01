import random

class Squirtle:
    
    def __init__(self):
        self._name = 'Squirtle'
        self._hp = 44
        self._attack = 48
        self._defense = 65
        self._special = 50
        self._speed = 43
        self._nickname = 'Squirtz'
        self._moveset = self._moveset = [{'Name': 'Tackle', 'Power': 40, 'Accuracy': 100, 'Type': 'Normal', 'Category': 'Physical'}], [{'Name': 'Tail Whip', 'Power': None, 'Accuracy': 100, 'Type': 'Normal', 'Category': 'Status'}]

    def __repr__(self):
        return f'You received a {self._name}!\nHP: {self._hp}\nAttack: {self._attack}\nDefense: {self._defense}\nSpecial: {self._special}\nSpeed: {self._speed}'
    
    def getName(self):
        return self._name
    
    def getNickname(self):
        return self._nickname

    def setNickname(self, newName):
        self._nickname = newName
        return self._nickname
    
    def getMoveset(self):
        return self._moveset

class Charmander:
    
    def __init__(self):
        self._name = 'Charmander'
        self._hp = 39
        self._attack = 52
        self._defense = 43
        self._special = 50
        self._speed = 65
        self._nickname = 'Chad'
        self._moveset = [{'Name': 'Scratch', 'Power': 40, 'Accuracy': 100, 'Type': 'Normal', 'Category': 'Physical'}], [{'Name': 'Growl', 'Power': None, 'Accuracy': 100, 'Type': 'Normal', 'Category': 'Status'}]

    def __repr__(self):
        return f'You received a {self._name}!\nHP: {self._hp}\nAttack: {self._attack}\nDefense: {self._defense}\nSpecial: {self._special}\nSpeed: {self._speed}'
    
    def getName(self):
        return self._name

    def getNickname(self):
        return self._nickname

    def setNickname(self, newName):
        self._nickname = newName
    
    def getMoveset(self):
        return self._moveset

class Bulbasaur:
    
    def __init__(self):
        self._name = 'Bulbasaur'
        self._hp = 45
        self._attack = 49
        self._defense = 49
        self._special = 65
        self._speed = 45
        self._nickname = 'Bulby'
        self._moveset = [{'Name': 'Tackle', 'Power': 40, 'Accuracy': 100, 'Type': 'Normal', 'Category': 'Physical'}], [{'Name': 'Growl', 'Power': None, 'Accuracy': 100, 'Type': 'Normal', 'Category': 'Status'}]

    def __repr__(self):
        return f'You received a {self._name}!\nHP: {self._hp}\nAttack: {self._attack}\nDefense: {self._defense}\nSpecial: {self._special}\nSpeed: {self._speed}'

    def getName(self):
        return self._name

    def getNickname(self):
        return self._nickname

    def setNickname(self, newName):
        self._nickname = newName
    
    def getMoveset(self):
        return self._moveset

def roll_starter(starters):
    yourStarter = random.choice(starters)
    yield yourStarter

generator = roll_starter((Squirtle(), Charmander(), Bulbasaur()))

for yourPoke in generator:
    print(yourPoke)

if yourPoke.getName() == 'Charmander':
    print('Rating: You got the best Pokemon starter...')
elif yourPoke.getName() == 'Squirtle':
    print('Rating: Now we\'re talking...') 
else:
    print('Rating: I mean it\'s all right...')

newNickname = input(f'\nWhat nickname (currently: {yourPoke.getNickname()}) would you like to give your Pokemon? ')
yourPoke.setNickname(newNickname)
print(f'You changed your {yourPoke.getName()}\'s nickname to {yourPoke.getNickname()}.')
print(f'Your starter Pokemon\'s moveset is: {yourPoke.getMoveset()}')

quit()

# test