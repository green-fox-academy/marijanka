import vector

class Ball():
    def __init__(self, x, y, radius):
        self.pos = (x, y)
        self.size = vector.multiply((radius, radius), 2)

    def get_bbox(self):
        start = vector.add(self.pos, vector.multiply(self.size, -0.5))
        end = vector.add(self.pos, vector.multiply(self.size, 0.5))
        return start + end
