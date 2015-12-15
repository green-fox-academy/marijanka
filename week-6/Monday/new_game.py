import random

class Character():
    def __init__(self, name, health, dexterity, luck):
        self.name = name
        self.health = health
        self.dexterity = dexterity
        self.luck = luck

def roll_stats():
    default_health = random.randint(2, 12) + 12
    
