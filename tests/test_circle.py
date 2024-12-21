import unittest
import math
import circle


class TestCircle(unittest.TestCase):

    def test_area(self):
        r = 5
        expected_area = math.pi * r * r
        result = circle.area(r)
        self.assertAlmostEqual(result, expected_area, places=5)

    def test_perimeter(self):
        r = 5
        expected_perimeter = 2 * math.pi * r
        result = circle.perimeter(r)
        self.assertAlmostEqual(result, expected_perimeter, places=5)

    def test_invalid_radius(self):
        r = -5
        with self.assertRaises(ValueError):
            circle.area(r)
            circle.perimeter(r)


if __name__ == "__main__":
    unittest.main()
