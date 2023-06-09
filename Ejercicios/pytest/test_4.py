import unittest
from ej4 import calculate_statistics

class test4(unittest.TestCase):
    def test_calculate_statistics(self):
        resultado1 = calculate_statistics([5,5,5,5])
        self.assertEqual(resultado1,(0.0, 5.0))

        resultado2 = calculate_statistics([5,6,7,8,9])
        self.assertEqual(resultado2,(1.4142135623730951, 7.0))