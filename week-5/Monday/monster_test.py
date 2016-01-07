import unittest
from monster import Monster

class TestBarbarian(unittest.TestCase):
    def test_existance(self):
        monster = Monster("Godzilla", 20, 1)

    def test_inharitance(self):
        monster = Monster("Godzilla", 20, 1)
        self.assertEqual(monster.hp, 20)

    def test_strike(self):
        monster = Monster("Godzilla", 20, 1)
        opponent = Monster("Randal", 10, 2)
        monster.strike(opponent)
        self.assertEqual(monster.hp, 22)
        self.assertEqual(opponent.hp, 9)


unittest.main()
