from geometric_lib.circle import area, perimeter
import unittest

class CirlceTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res1 = area(0)
        res2 = perimeter(0)
        self.assertEqual(res1, 0)
        self.assertEqual(res2, 0)
    
    def test_calculation(self):
        res1 = area(4)
        res2 = perimeter(4)
        self.assertEqual(res1, 50.26548245743669)
        self.assertEqual(res2, 25.132741228718345)
    
    def test_big_numbers(self):
        res1 = area(10000000000)
        res2 = perimeter(100)
        self.assertEqual(res1, 3.1415926535897933e+20)
        self.assertEqual(res2, 628.3185307179587)
    
    def test_negative_numbers(self):
        with self.assertRaises(ValueError):
            area(-1)
            perimeter(-1)
    
    def test_invalid_input_none(self):
        with self.assertRaises(TypeError):
            area(None)
            perimeter(None)

    def test_invalid_input_str(self):
        with self.assertRaises(TypeError):
            area("12")
            perimeter("11")