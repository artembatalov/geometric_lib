from geometric_lib.square import area, perimeter
import unittest

class SquareTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res1 = area(0)
        res2 = perimeter(0)
        self.assertEqual(res1, 0)
        self.assertEqual(res2, 0)
    
    def test_calculation(self):
        res1 = area(4)
        res2 = perimeter(4)
        self.assertEqual(res1, 16)
        self.assertEqual(res2, 16)
    
    def test_big_numbers(self):
        res1 = area(10000000000)
        res2 = perimeter(100000000)
        self.assertEqual(res1, 100000000000000000000)
        self.assertEqual(res2, 400000000)