print("ejercicio 1")

def buscarValor(numero):
   print(lista.index(numero))

lista = [1,2,3,4,5,6]
numero = int(input("Ingrese un numero: "))
buscarValor(numero)

print("ejercicio 2")

def bisiesto(anio):
    if((anio%4) == 0 & (anio%100 != 0 | (anio%400) == 0)):
        print("bisiesto")

año = int(input("ingrese año"))
bisiesto(año)

print("ejercicio 3")

def dibujar(alto, ancho, caracter):
    for i in range(alto):
        print(caracter * ancho)

alto = int(input("alto "))
ancho = int(input("ancho "))
caracter = input("caracter ")
print("\n")
dibujar(alto, ancho, caracter)

print("ejercicio 4")

tamaño = int(input("tamaño lista "))
lista = []
for i in range(tamaño):
    numero = int(input("ingrese un numero "))
    lista.append(numero)
def ordenar(lista : list):
    lista.sort()
    print(lista)
    
ordenar(lista)
        
print("ejercicio 5")


def espalindrome(palabra):
    palabra.lower()
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        print("es palindrome")
    else:
        print("NO ES PALINDROME")
        
palabra = input("ingrese la palabra para ver si es palindrome: ")
espalindrome(palabra)

print("ejercicio 6")

vocales = "aeiouAEIOU"
def contarVocales(cadena : str):
    contador = 0
    for letra in cadena:
        if letra in vocales:
            contador += 1
    print(f"la frase {frase} tiene {contador} vocales")
frase = input("ingrese una frase para saber cuantas vocales tiene   ")
contarVocales(frase)

print("ejercicio 7")

def esStep(numero : int):
    str = str(numero)
    for i in range(len(str) - 1):
        if abs(int(str[i]) - int(str[i + 1])) != 1:
            return False
    return True

print(esStep(123234))
