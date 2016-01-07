import unittest
from wizard import Wizard

class TestWizard(unittest.TestCase):
    def test_existance(self):
        wizard = Wizard("Merlin", 40, 10, 20)

    def test_inharitance(self):
        wizard = Wizard("Merlin", 40, 10, 20)
        self.assertEqual(wizard.hp, 40)

    def test_manna(self):
        wizard = Wizard("Merlin", 40, 10, 20)
        self.assertEqual(wizard.manna, 20)

    def test_strike(self):
        wizard = Wizard("Merlin", 40, 2, 20)
        opponent = Wizard("Dumbledor", 10, 2, 10)
        wizard.strike(opponent)
        self.assertEqual(opponent.hp, 4)

    def test_strike_2(self):
        wizard = Wizard("Voldemort", 40, 10, 3)
        opponent = Wizard("Hermioner", 9, 2, 10)
        wizard.strike(opponent)
        self.assertEqual(opponent.hp, 6)

    def test_strike_3(self):
        wizard = Wizard("Voldemort", 40, 10, 3)
        opponent = Wizard("Hermioner", 9, 2, 10)
        wizard.strike(opponent)
        self.assertEqual(wizard.manna, 3)

    def test_strike_4(self):
        wizard = Wizard("Harry", 40, 10, 25)
        opponent = Wizard("Hermioner", 9, 2, 10)
        wizard.strike(opponent)
        self.assertEqual(wizard.manna, 20)



unittest.main()
