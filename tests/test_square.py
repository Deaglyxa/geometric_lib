import unittest
import square


class TestSquare(unittest.TestCase):
    def test_area(self):
        a = 4
        expected_area = a * a
        result = square.area(a)
        self.assertEqual(result, expected_area)

    def test_perimeter(self):
        a = 4
        expected_perimeter = 4 * a
        result = square.perimeter(a)
        self.assertEqual(result, expected_perimeter)

    def test_invalid_side_area(self):
        with self.assertRaises(ValueError):
            square.area(-1)

    def test_invalid_side_perimeter(self):
        with self.assertRaises(ValueError):
            square.perimeter(-1)


if __name__ == "__main__":
    unittest.main()
