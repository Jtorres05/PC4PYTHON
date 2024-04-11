import random
from pyfiglet import Figlet

# Obtener la lista de fuentes disponibles
figlet = Figlet()
fuentes_disponibles = figlet.getFonts()

# Solicitar al usuario el nombre de la fuente o seleccionar una aleatoria si no se proporciona
fuente = input(f"Ingrese el nombre de la fuente (o presione Enter para seleccionar una aleatoria): ")
if not fuente:
    fuente = random.choice(fuentes_disponibles)

# Verificar si la fuente proporcionada por el usuario está en la lista de fuentes disponibles
if fuente not in fuentes_disponibles:
    print("La fuente ingresada no es válida. Seleccione una de las siguientes fuentes:")
    print(fuentes_disponibles)
    exit()

# Solicitar al usuario el texto a imprimir
texto = input("Ingrese el texto que desea imprimir: ")

# Configurar la fuente seleccionada
figlet.setFont(font=fuente)

# Imprimir el texto usando la fuente seleccionada
print(figlet.renderText(texto))
