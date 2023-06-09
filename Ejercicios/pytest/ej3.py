class Anagram():
    def is_anagram(word1 : str, word2 : str):
        
        word1 = word1.lower()
        word2 = word2.lower()
        
        
        lista1 = list(word1)
        lista2 = list(word2)
        
        lista1.sort()
        lista2.sort()
        
        if lista1 == lista2:
            print("true")
            return True
        else:
            print("false")
            return False