from character import Character

class Wizard(Character):
    def __init__(self, name, hp, damage, manna):
        super().__init__(name, hp, damage)
        self.manna = manna

    def strike(self, opponent):
        if self.manna > 4:
            opponent.hp -= 3 * self.damage
            self.manna -= 5
        else:
            opponent.hp -= int(self.damage / 3)
