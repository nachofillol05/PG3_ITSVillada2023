import unittest
from ej3 import Anagram

class Test_password(unittest.TestCase):
    def setUp(self) -> None:
        self.anagram = Anagram()
        
    def isAnagram(self):
        resultado1 = self.anagram.is_anagram("jose", "osej")
        self.assertEqual(resultado1, True)
        resultado2 = self.anagram.is_anagram("jose", "juhkj")
        self.assertEqual(resultado2, False)
        
        