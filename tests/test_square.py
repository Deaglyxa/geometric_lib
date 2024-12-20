import unittest
from square import area, perimeter

class TestSquareCalculations(unittest.TestCase):

    def test_area_positive_side(self):
        side = 3
        expected_area = side * side
        res = area(side)
        self.assertEqual(res, expected_area)

    def test_area_zero_side(self):
        side = 0
        expected_area = 0
        res = area(side)
        self.assertEqual(res, expected_area)

    def test_area_negative_side(self):
        side = -2
        with self.assertRaises(ValueError):
            area(side)

    def test_perimeter_positive_side(self):
        side = 3
        expected_perimeter = 4 * side
        res = perimeter(side)
        self.assertEqual(res, expected_perimeter)

    def test_perimeter_zero_side(self):
        side = 0
        expected_perimeter = 0
        res = perimeter(side)
        self.assertEqual(res, expected_perimeter)

    def test_perimeter_negative_side(self):
        side = -2
        with self.assertRaises(ValueError):
            perimeter(side)
