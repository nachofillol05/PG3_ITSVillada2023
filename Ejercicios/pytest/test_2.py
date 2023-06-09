import unittest
from ej2 import roman_to_decimal

class Test_decimal(unittest.TestCase):
    def test_roman_to_decimal(self):
        resultado1 = roman_to_decimal('MXVII')
        self.assertEqual(resultado1, 1017)
        
        resultado2 = roman_to_decimal('CXXIX')
        self.assertEqual(resultado2, 129)
