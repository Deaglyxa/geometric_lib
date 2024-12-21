import unittest
import calculate


class TestCalculate(unittest.TestCase):
    def test_calc_circle_area(self):
        fig = "circle"
        func = "area"
        size = [5]
        expected_result = 3.141592653589793 * 5 * 5
        result = calculate.calc(fig, func, size)
        self.assertAlmostEqual(result, expected_result, places=5)

    def test_calc_square_perimeter(self):
        fig = "square"
        func = "perimeter"
        size = [4]
        expected_result = 4 * 4
        result = calculate.calc(fig, func, size)
        self.assertEqual(result, expected_result)

    def test_invalid_figure(self):
        fig = "hexagon"
        func = "area"
        size = [5]
        with self.assertRaises(AssertionError):
            calculate.calc(fig, func, size)

    def test_invalid_function(self):
        fig = "circle"
        func = "volume"
        size = [5]
        with self.assertRaises(AssertionError):
            calculate.calc(fig, func, size)

    def test_invalid_size(self):
        fig = "circle"
        func = "area"
        size = [5, 5]
        with self.assertRaises(TypeError):
            calculate.calc(fig, func, size)


if __name__ == "__main__":
    unittest.main()
