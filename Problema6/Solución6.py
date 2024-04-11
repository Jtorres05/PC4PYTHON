def contar_lineas_codigo(ruta_archivo):
    if not ruta_archivo.endswith(".py"):
        print("El archivo no tiene extensión .py")
        return

    try:
        with open(ruta_archivo, "r") as file:
            lineas_codigo = 0
            for linea in file:
                linea = linea.strip()
                if linea and not linea.startswith("#"):
                    lineas_codigo += 1
        return lineas_codigo
    except FileNotFoundError:
        print("No se encontró el archivo.")
        return

ruta_archivo = input("Ingrese la ruta del archivo .py: ")
cantidad_lineas = contar_lineas_codigo(ruta_archivo)
if cantidad_lineas is not None:
    print(f"El número de líneas de código en el archivo '{ruta_archivo}' es: {cantidad_lineas}")