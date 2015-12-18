import random

class Character():
    def __init__(self, name = None):
        self.name = name
        self.health = 0
        self.dexterity = 0
        self.health_start = 0
        self.stats = {'Health': 0, 'Dexterity': 0}
        self.stats_start = {'Health_start': 0, 'Dexterity': 0}

    def dice(self):
        return random.randint(1, 6)

    def game_dice(self):
        return random.randint(1, 6) + random.randint(1, 6) + 6

    def roll_stats(self):
        self.health = self.dice() + self.dice() + 12
        self.health_start = self.health
        self.stats['Health'] = self.health
        self.stats_start['Health_start'] = self.health_start
        self.dexterity = self.dice() + 6
        self.stats['Dexterity'] = self.dexterity
        self.stats_start['Dexterity'] = self.dexterity

    def display_roll_stats(self):
        print('\n' + self.name + '\n')
        print('\n'.join(['{} {}'.format(item, self.stats[item]) for item in self.stats])+'\n')
        print('\n'.join(['{} {}'.format(item, self.stats_start[item]) for item in self.stats_start])+'\n')

class Player(Character):
    def __init__(self):
        super().__init__()
        self.luck = 0
        self.luck_start = 0
        self.inventory = {'Weapon':'Sward', 'Armor':'Leathor Armor', 'potion': None}
        self.stats = {'Health': 0, 'Dexterity': 0, 'Luck': 0}
        self.stats_start = {'Health_start': 0, 'Dexterity': 0, 'Luck_start': 0}

    def roll_stats(self):
        super().roll_stats()
        self.luck = self.dice() + 6
        self.luck_start = self.luck
        self.stats['Luck'] = self.luck
        self.stats_start['Luck_start'] = self.luck_start

    def character_stats(self):
        print(self.inventory['Weapon'] + '\n' + self.inventory['Armor'] + '\n' + self.inventory['potion'] + '\n')

class Monster(Character):
    def get_name(self):
        self.name = 'Godzi'
        return self.name

user = Player()
monster = Monster()
