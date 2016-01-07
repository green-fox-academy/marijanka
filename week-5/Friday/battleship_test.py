import unittest
import battleship

class TestBattlessip(unittest.TestCase):
    def setUp(self):
        self.field = [
                        [1,1,0,1,0,0,1,1,1,1],
                        [0,0,0,1,0,0,0,0,0,0],
                        [1,0,0,1,0,1,1,1,0,1],
                        [1,0,0,0,0,0,0,0,0,1],
                        [1,0,0,0,0,0,0,0,0,0],
                        [1,0,0,0,0,1,0,0,0,1],
                        [0,0,0,0,0,1,0,0,0,1],
                        [1,1,0,0,0,0,0,0,0,1],
                        [0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,1,1,1,1,1,1]
                      ]


    def test_instantiante(self):
        self.assertIsInstance(battleship.Field([]), battleship.Field)
        self.assertIsInstance(battleship.ShipField(), battleship.ShipField)

unittest.main()
