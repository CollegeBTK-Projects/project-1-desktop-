import unittest
from calculator import calculate

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculate("1+1"), "2")
    def test_multiply(self):
        self.assertEqual(calculate("2*3"), "6")
    def test_divide(self):
        self.assertEqual(calculate("10/2"), "5.0")
    def test_subtract(self):
        self.assertEqual(calculate("5-3"), "2")
    def test_order_of_operations(self):
        self.assertEqual(calculate("2+2*2"), "6")
    def test_division_by_zero(self):
        self.assertEqual(calculate("10/0"), "Ошибка")

