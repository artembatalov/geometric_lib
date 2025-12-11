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