class Field:
    def __init__(self, position, ship_status, shot_status):
        self.position = position
        self.ship_status = ship_status
        self.shot_status = shot_status

class ShipField(Field):
    pass
