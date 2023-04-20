meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
def mes(num_mes : int):
    try:
        nombre_mes = meses[num_mes - 1]
        print("El nombre del mes es: ", nombre_mes)

    except IndexError:
        print("Error: El número de mes ingresado está fuera del rango válido.")
        
        
if __name__ == "__main__":
    mes(int(input("Ingrese el número del mes (1-12): ")))
