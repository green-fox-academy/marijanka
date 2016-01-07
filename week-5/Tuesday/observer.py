import random

class Warrior:
    def __init__(self):
        self.companions = []
        self.hp = 100

    def join(self, companion):
        self.companions.append(companion)

    def strike(self, opponent):
        opponent.inflict_damage(10)

    def inflict_damage(self, damage):
        self.hp -= damage
        self.notify_all("damage")

    def heal(self, hp):
        self.hp += hp

    def notify_all(self, type):
        for companion in self.companions:
            companion.notify("type", self)

    def search_gold(self):
        if random.randint(1, 10) > 5:
            for companion in self.companions:
                    companion.notify("find Gold!", self)

    def curse(self, opponent):
        opponent.join(Witch())
        self.notify_all("curse")

class Healer:
    def notify(self, type, warrior):
        if type == "damage":
            warrior.heal(10)

class Witch:
    def notify(self, type, warrior):
        if type == "damage":
            warrior.heal(-10)

def Cheer:
    def notify(self, type, warrior):
        if type == "curse":
            print("Cool!!")



rabbit = Warrior()
wolf = Warrior()
shaman = Healer()
regina = Witch()

rabbit.join(shaman)

wolf.curse(rabbit)
wolf.strike(rabbit)
rabbit.search_gold()
print(rabbit.hp)
