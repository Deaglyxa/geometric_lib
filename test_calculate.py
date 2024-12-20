import unittest
from unittest.mock import patch
from calculate import calc

class TestCalculate(unittest.TestCase):

    def test_calc_valid_circle_area(self):

        fig = "circle"
        func = "area"
        size = [3]
        expected_result = 28.274333882308138

        with patch('builtins.print') as mock_print:
            calc(fig, func, size)

        mock_print.assert_called_once_with(f'area of circle is {expected_result}')

    def test_calc_valid_square_perimeter(self):

        fig = "square"
        func = "perimeter"
        size = [4]
        expected_result = 16

        with patch('builtins.print') as mock_print:
            calc(fig, func, size)

        mock_print.assert_called_once_with(f'perimeter of square is {expected_result}')

    def test_calc_invalid_figure(self):

        fig = "triangle"
        func = "area"
        size = [3]

        with self.assertRaises(AssertionError):
            calc(fig, func, size)

    def test_calc_invalid_function(self):

        fig = "circle"
        func = "volume"
        size = [3]

        with self.assertRaises(AssertionError):
            calc(fig, func, size)

    def test_calc_invalid_size_length(self):

        fig = "circle"
        func = "area"
        size = [3, 4]

        with self.assertRaises(TypeError):
            calc(fig, func, size)

    def test_calc_invalid_size_type(self):

        fig = "circle"
        func = "area"
        size = ["radius"]

        with self.assertRaises(TypeError):
            calc(fig, func, size)

