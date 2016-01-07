from character import Character

class Clerlic(Character):
    def heal(self, other):
        other.hp += 10
