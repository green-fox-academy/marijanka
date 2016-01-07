class Character():
    def __init__(self, health = 20, armor = 10):
        self._health = health
        self._armor = armor
        self._isAlive = True

    def sufferDamage(self, damage):
        sufferDamage = self._health + self._armor - damage
        if sufferDamage < 1:
            self._isAlive = False

    def heal(self, heal):
        self._health += heal

    def isAlive(self):
        return self._isAlive

def handleEvents(events):
    damage_list = list(filter(lambda event : event['type'] == 'damage', events))
    #list(map(lambda event['character'].sufferDamage(event['size']), damage))
    for event in damage_list:
        event['character'].sufferDamage(event['size'])
