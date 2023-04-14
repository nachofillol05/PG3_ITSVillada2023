def DivisionNumeros():
    while True:
            try:
                n1 = int(input("Ingrese el primer numero "))
                n2 = int(input("Ingrese el segundo numero "))
                print(f"la division da {str(n1/n2)}")
                
                if(input("quiere continuar?") != "si"):
                    break
            except ValueError:
                print("Ingrese un numero no otra cosa porfavor")
            except ZeroDivisionError:
                print("el segundo numero no puede ser 0")
    
    
if __name__ == "__main__":
    DivisionNumeros()     