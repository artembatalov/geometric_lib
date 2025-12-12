from geometric_lib.triangle import area, perimeter
import unittest

class TriangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res1 = area(0, 0)
        res2 = perimeter(0, 0, 0)
        self.assertEqual(res1, 0)
        self.assertEqual(res2, 0)
    
    def test_calculation(self):
        res1 = area(4, 2)
        res2 = perimeter(4, 2, 4)
        self.assertEqual(res1, 4)
        self.assertEqual(res2, 10)
    
    def test_big_numbers(self):
        res1 = area(10000000000, 200)
        res2 = perimeter(100, 1000000000, 100000000000000000)
        self.assertEqual(res1, 1000000000000)
        self.assertEqual(res2, 100000001000000100)
    
    def test_negative_numbers(self):
        with self.assertRaises(ValueError):
            area(-1, 5)
            perimeter(-1, 5. -1)
    
    def test_invalid_input_none(self):
        with self.assertRaises(TypeError):
            area(None, 5)
            perimeter(5, 4, None)

    def test_invalid_input_str(self):
        with self.assertRaises(TypeError):
            area("12", "12")
            perimeter("12", "12", "1")