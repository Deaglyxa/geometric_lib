import unittest
from unittest.mock import patch
from calculate import calc


class TestCalculate(unittest.TestCase):
    """
    Test case for testing the 'calc' function from the 'calculate' module.
    Includes tests for valid and invalid input for various figures and functions.
    """

    def test_calc_valid_circle_area(self):
        """
        Test the calculation of the area of a circle with a valid input.
        """
        fig = "circle"
        func = "area"
        size = [3]
        expected_result = 28.274333882308138

        with patch('builtins.print') as mock_print:
            calc(fig, func, size)

        mock_print.assert_called_once_with(f'area of circle is {expected_result}')

    def test_calc_valid_square_perimeter(self):
        """
        Test the calculation of the perimeter of a square with a valid input.
        """
        fig = "square"
        func = "perimeter"
        size = [4]
        expected_result = 16

        with patch('builtins.print') as mock_print:
            calc(fig, func, size)

        mock_print.assert_called_once_with(f'perimeter of square is {expected_result}')

    def test_calc_invalid_figure(self):
        """
        Test for invalid figure type (e.g., 'triangle').
        """
        fig = "triangle"
        func = "area"
        size = [3]

        with self.assertRaises(AssertionError):
            calc(fig, func, size)

    def test_calc_invalid_function(self):
        """
        Test for invalid function type (e.g., 'volume').
        """
        fig = "circle"
        func = "volume"
        size = [3]

        with self.assertRaises(AssertionError):
            calc(fig, func, size)

    def test_calc_invalid_size_length(self):
        """
        Test for invalid number of size parameters.
        """
        fig = "circle"
        func = "area"
        size = [3, 4]

        with self.assertRaises(TypeError):
            calc(fig, func, size)

    def test_calc_invalid_size_type(self):
        """
        Test for invalid type of size parameters.
        """
        fig = "circle"
        func = "area"
        size = ["radius"]

        with self.assertRaises(TypeError):
            calc(fig, func, size)
