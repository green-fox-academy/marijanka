import unittest
from decoded import MyMagic

class TestDecoded(unittest.TestCase):
    def setUp(self):
        self.strings = 'recede'

    def test_coded(self):
        self.assertEqual(MyMagic.encoded(self.strings), '()()()')

unittest.main()
