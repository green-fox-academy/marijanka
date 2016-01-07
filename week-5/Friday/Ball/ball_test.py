import unittest
from ball import Ball

class TestBall(unittest.TestCase):
    def test_exits(self):
        ball = Ball(40, 50, 10)

    def test_position_and_size(self):
        ball = Ball(40, 50, 10)
        self.assertEqual(ball.pos, (40, 50))
        self.assertEqual(ball.size, (20, 20))

    def test_get_bbox(self):
        ball = Ball(40, 50, 10)
        bbox = ball.get_bbox()
        self.assertEqual(bbox, (30, 40, 50, 60))

    def test_velocity(self):


unittest.main()
