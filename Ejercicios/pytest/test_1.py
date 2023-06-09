import unittest
from ej1 import validate_password

class Test_password(unittest.TestCase):
    def Test_login(self):
        resultado1 = validate_password("Juancito123")
        self.assertEqual(True, resultado1)
        
        resultado2 = validate_password("Juancito")
        self.assertEqual(False, resultado2)
        
        resultado3 = validate_password("JUANCITO")
        self.assertEqual(False, resultado3)
        
        resultado4 = validate_password("Juancito123#")
        self.assertEqual(False, resultado4)

        
    
        