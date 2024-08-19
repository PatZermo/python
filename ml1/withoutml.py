# Please read the README. Here we convert Celsius to Fahrenheit and vice versa using traditional programming.

def menu():
    while True:
        seleccion = input("Elegí la tarea: \n1. Celsius a Farenheit \n2. Farenheit a Celsius \n3. Salir ")
        if seleccion == "1":
            convertirCaF()
        elif seleccion == "2":
            convertirFaC()
        elif seleccion == "3":
            break
        else:
            print("Solo es posible seleccionar las opciones 1, 2 o 3.")

def convertirCaF():
    convertir = float(input("Ingresa grados celsius: "))
    resultado = convertir * 1.8 + 32
    print(resultado)

def convertirFaC():
    convertir = float(input("Ingresa grados farenheit: "))
    resultado = (convertir - 32) * 0.55
    print(resultado)

menu()