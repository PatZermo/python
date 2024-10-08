#Here, the programmer has already preloaded the necessary mathematical operations to convert from Celsius to Fahrenheit and from 
#Fahrenheit to Celsius. The user can input temperatures, and they will be converted using the preloaded functions.

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

#Mathematical operations

def convertirCaF():
    convertir = float(input("Ingresa grados celsius: "))
    resultado = convertir * 1.8 + 32
    print(f"{convertir} grados celsius son: {resultado} grados farenheit")

def convertirFaC():
    convertir = float(input("Ingresa grados farenheit: "))
    resultado = (convertir - 32) * 0.55
    print(f"{convertir} grados farenheit son: {resultado} grados celsius")

menu()
