import unittest
from triangle import area, perimeter


class TestTriangleCalculations(unittest.TestCase):

    def test_area_valid_triangle(self):
        a, b, c = 3, 4, 5
        expected_area = 6.0

        result = area(a, b, c)

        self.assertAlmostEqual(result, expected_area, places=5)

    def test_area_invalid_triangle(self):
        a, b, c = 1, 2, 10

        with self.assertRaises(ValueError):
            area(a, b, c)

    def test_area_zero_side(self):
        a, b, c = 0, 4, 5

        with self.assertRaises(ValueError):
            area(a, b, c)

    def test_perimeter_valid_triangle(self):
        a, b, c = 3, 4, 5
        expected_perimeter = 12

        result = perimeter(a, b, c)

        self.assertEqual(result, expected_perimeter)

    def test_perimeter_invalid_triangle(self):
        a, b, c = 1, 2, 10

        with self.assertRaises(ValueError):
            perimeter(a, b, c)

    def test_perimeter_zero_side(self):
        a, b, c = 0, 4, 5

        with self.assertRaises(ValueError):
            perimeter(a, b, c)
