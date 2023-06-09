import unittest
from ej5 import search_matrix

class test5(unittest.TestCase):
        
    def test_search_matrix(self):
        resultado1 = search_matrix([1,7,2,7,954],2)
        self.assertEqual(resultado1,True)

        resultado2 = search_matrix([543,1212,232344,2413],3)
        self.assertEqual(resultado2,False)