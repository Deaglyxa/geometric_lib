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
        a, b, c = -3, 4, 5
        with self.assertRaises(ValueError):
            triangle.area(a, b, c)
            triangle.perimeter(a, b, c)


if __name__ == "__main__":
    unittest.main()
