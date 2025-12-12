from geometric_lib.rectangle import area, perimeter
import unittest

class RectangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res1 = area(0, 100)
        res2 = perimeter(0, 0)
        self.assertEqual(res1, 0)
        self.assertEqual(res2, 0)
    
    def test_diffirent_number_input(self):
        res1 = area(4, 5)
        res2 = perimeter(4, 5)
        self.assertEqual(res1, 20)
        self.assertEqual(res2, 18)

    def test_even_number(self):
        res1 = area(2, 2)
        res2 = perimeter(2, 2)
        self.assertEqual(res1, 4)
        self.assertEqual(res2, 8)
    
    def test_big_numbers(self):
        res1 = area(10000000000, 100000000)
        res2 = perimeter(10000000000, 100000000)
        self.assertEqual(res1, 1000000000000000000)
        self.assertEqual(res2, 20200000000)

    def test_negative_numbers(self):
        with self.assertRaises(ValueError):
            area(-1, 5)
            perimeter(-1, 5)
    
    def test_invalid_input_none(self):
        with self.assertRaises(TypeError):
            area(None, 5)
            perimeter(None, 5)

    def test_invalid_input_str(self):
        with self.assertRaises(TypeError):
            area("12", "12")
            perimeter("12", "12")
    