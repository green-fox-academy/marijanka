class Game_character:
    def __init__(self, name, health_points, demage):
        self.name = name
        self.health_points = health_points
        self.demage = demage

    def drink_potion(self):
        self.health_points += 10

    def strike(self, other):
        other.health_points -= self.demage
        print('Enemy hp :' + str(self.health_points))

    def print_status(self):
        if self.health_points <= 0:
            print(self.name, ':', 'Dead')
        else: print(self.name, ':', str(self.health_points))

class Cerlic(Game_character):
    def heal(self, ally):
        ally.health_points += 10
        print('Ally hp :', str(ally.health_points))

barlog = Game_character('Barlog', 100, 20)
gandalf = Game_character('Gandalf the Grey', 50, 40)
melkor = Cerlic('Melkor', 1000, 80)

barlog.print_status()
for i in range(3):
    gandalf.strike(barlog)
    melkor.heal(barlog)
barlog.print_status()
