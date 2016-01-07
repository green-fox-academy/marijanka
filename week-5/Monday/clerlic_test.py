import unittest
from clerlic import Clerlic

class TestClerlic(unittest.TestCase):
    def test_existance(self):
        clerlic = Clerlic('Test', 100, 10)

    def test_inharitance(self):
        clerlic = Clerlic('Test', 100, 10)
        self.assertEqual(clerlic.hp, 100)

    def test_heal(self):
        clerlic = Clerlic('Test', 100, 10)
        other = Clerlic('Other', 100, 10)
        clerlic.heal(other)
        self.assertEqual(other.hp, 110)

unittest.main()
