def guardar_tabla_multiplicar(numero):
    if numero < 1 or numero > 10:
        print("El número debe estar entre 1 y 10.")
        return

    with open(f"tabla-{numero}.txt", "w") as file:
        for i in range(1, 11):
            file.write(f"{numero} x {i} = {numero*i}\n")

    print(f"Tabla de multiplicar del {numero} guardada en 'tabla-{numero}.txt'")

def mostrar_tabla_multiplicar(numero):
    try:
        with open(f"tabla-{numero}.txt", "r") as file:
            print(file.read())
    except FileNotFoundError:
        print(f"No se encontró el archivo 'tabla-{numero}.txt'.")

def mostrar_linea_tabla_multiplicar(numero, linea):
    try:
        with open(f"tabla-{numero}.txt", "r") as file:
            lineas = file.readlines()
            if len(lineas) >= linea:
                print(lineas[linea - 1])
            else:
                print(f"La línea {linea} no existe en el archivo 'tabla-{numero}.txt'.")
    except FileNotFoundError:
        print(f"No se encontró el archivo 'tabla-{numero}.txt'.")


def menu():
    print("1. Guardar tabla de multiplicar")
    print("2. Mostrar tabla de multiplicar")
    print("3. Mostrar línea de tabla de multiplicar")
    print("4. Salir")


while True:
    menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        numero = int(input("Ingrese un número entre 1 y 10: "))
        guardar_tabla_multiplicar(numero)
    elif opcion == "2":
        numero = int(input("Ingrese un número entre 1 y 10: "))
        mostrar_tabla_multiplicar(numero)
    elif opcion == "3":
        numero = int(input("Ingrese un número entre 1 y 10: "))
        linea = int(input("Ingrese el número de línea a mostrar: "))
        mostrar_linea_tabla_multiplicar(numero, linea)
    elif opcion == "4":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
