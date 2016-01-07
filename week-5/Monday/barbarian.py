from character import Character

class Barbarian(Character):
    def strike(self, opponent):
        opponent.hp -= 2 * self.damage
