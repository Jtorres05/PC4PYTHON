import requests
import zipfile
from io import BytesIO
import os

# Descargar la imagen desde la URL
url = "https://images.unsplash.com/photo-1546527868-ccb7ee7dfa6a?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
response = requests.get(url)

# Verificar si la descarga fue exitosa
if response.status_code == 200:
    # Crear un objeto ZipFile en modo de escritura
    with zipfile.ZipFile("imagen.zip", "w") as zip_file:
        # Agregar la imagen descargada al archivo ZIP
        zip_file.writestr("imagen.jpg", response.content)

    print("Imagen descargada y comprimida exitosamente como imagen.zip")

    # Descomprimir el archivo ZIP
    with zipfile.ZipFile("imagen.zip", "r") as zip_file:
        zip_file.extractall("unzipped_image")

    print("Archivo ZIP descomprimido exitosamente en la carpeta 'unzipped_image'")
else:
    print("No se pudo descargar la imagen")

