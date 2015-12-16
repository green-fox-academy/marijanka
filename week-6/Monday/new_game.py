import random

class Character():
    def __init__(self, name, health=0, dexterity=0, luck=0):
        self.name = name
        self.health = health
        self.dexterity = dexterity
        self.luck = luck

        self.health_start = health
        self.dexterity_start = dexterity
        self.luck_start = luck
        self.inventory = {'Weapon':'Sword', 'Armor':'Leather Armor', 'potion': None}

user = Character('')

def dice():
    return random.randint(1, 6)

def roll_stats():
    print('\n' + user.name + ' ezek az alap pontjaid:' + '\n')
    roll = dice()
    user.health = roll * 2 + 12
    user.health_start = user.health
    print('Életerő pontszámaid: ', user.health_start)
    user.dexterity = roll + 6
    user.dexterity_start = user.dexterity
    print('Ügyességi pontszámaid: ', user.dexterity_start)
    user.luck = roll + 6
    user.luck_start = user.luck
    print('Szerencse pontszámaid: ', user.dexterity_start, '\n')

def character_stats():
    roll_stats()
    print('és ezek az alap felszereléseid: ')
    print('\n' + user.inventory['Weapon'])
    print(user.inventory['Armor'])
    if user.inventory['potion'] == 1:
        print('Életerő főzet' + '\n')
    elif user.inventory['potion'] == 2:
        print('Ügyesség főzet' + '\n')
    elif user.inventory['potion'] == 3:
        print('Szerencse Főzet' + '\n')
