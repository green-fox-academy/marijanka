import sudoku_checker
import unittest

class TestSudokuChecker(unittest.TestCase):
    def test_is_complete_empty(self):
        test_input = []
        expected = False
        actual = sudoku_checker.is_complete(test_input)
        self.assertEqual(expected, actual, "The row is empty.")

    def test_is_complete_too_short(self):
        test_input = [1, 2, 3, 4, 5, 6, 7, 8]
        expected = False
        actual = sudoku_checker.is_complete(test_input)
        self.assertEqual(expected, actual, "The row is too short.")

    def test_is_complete_too_much(self):
        test_input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        expected = False
        actual = sudoku_checker.is_complete(test_input)
        self.assertEqual(expected, actual, "The row is too much.")

    def test_is_complete_duplicate(self):
        test_input = [1, 2, 4, 4, 5, 6, 7, 8, 9]
        expected = False
        actual = sudoku_checker.is_complete(test_input)
        self.assertEqual(expected, actual, "In The row is duplicate.")

    def test_is_complete_integer(self):
        test_input = [1.2, 2, 4.4, 4, 5, 6, 7, 8, 9]
        expected = False
        actual = sudoku_checker.is_complete(test_input)
        self.assertEqual(expected, actual, "In The row is float.")

    def test_is_complete(self):
        test_input = [1, 2, 4, 3, 5, 6, 7, 8, 9]
        expected = True
        actual = sudoku_checker.is_complete(test_input)
        self.assertEqual(expected, actual)







unittest.main()
