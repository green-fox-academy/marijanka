import unittest
from practice import Mymagic

class TestPractice(unittest.TestCase):
    def setUp(self):
        self.names = [{'id': 1, 'name': 'John'},
                      {'id': 2, 'name': 'Molly'},
                      {'id': 3, 'name': 'Jane'}]
        self.subject = Mymagic(self.names)

    def test_instantiante(self):
        self.assertIsInstance(Mymagic([]), Mymagic)

    def test_names_as_list_when_empty(self):
        subject = Mymagic([])
        self.assertEqual(subject.name_lists(), [])

    def test_names_as_list(self):
        subject = Mymagic(self.names)
        self.assertEqual(subject.name_lists(), ['John', 'Molly', 'Jane'])

    def test_names_starts_with_j(self):
        subject = Mymagic(self.names)
        self.assertEqual(subject.name_lists_j(), ['John', 'Jane'])

unittest.main()
