import unittest
from menu import Menu
from menu import MenuItem

class TestMenu(unittest.TestCase):
    def test_invoke(self):
        def test_func():
            return True

        menu = Menu([
            MenuItem(1, 'Test', lambda: True)
        ])
        self.assertEqual(menu.invoke(1), True)


unittest.main()
