with open("archivoEscribir.txt", "w") as archivo:
    strings = ["Escrito", "con", "write"]
    for palabra in strings:
        try:
            archivo.write(palabra + "\n")
        except TypeError:
            print("Error: no se puede escribir un tipo de dato no compatible en un archivo de texto.")
