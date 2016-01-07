import unittest
from decorator import *

class TestUzi(unittest.TestCase):
    def test_uzi_effect(self):
        weapon = Uzi(TestWeapon())
        self.assertEqual(5, weapon.damage())

class TestWeapon:
    def damage(self):
        return 10

class TestMace:
    def damage(self):
        return 30

if __name__ == '__main__':
    unittest.main()
