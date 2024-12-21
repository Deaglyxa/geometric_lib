import unittest
import triangle


class TestTriangle(unittest.TestCase):
    def test_area(self):
        a, b, c = 3, 4, 5
        expected_area = (a + b + c) / 2
        result = triangle.area(a, b, c)
        self.assertEqual(result, expected_area)

    def test_perimeter(self):
        a, b, c = 3, 4, 5
        expected_perimeter = a + b + c
        result = triangle.perimeter(a, b, c)
        self.assertEqual(result, expected_perimeter)

    def test_invalid_sides(self):
        with self.assertRaises(ValueError):
            triangle.area(-1, 2, 3)
        with self.assertRaises(ValueError):
            triangle.area(1, 1, 3)

if __name__ == "__main__":
    unittest.main()
