import requests
import sqlite3

def obtener_datos_sunat():
    # URL de la API de SUNAT para obtener información del dólar
    url = "https://api.apis.net.pe/v1/tipo-cambio-sunat?month=2&year=2023"

    try:
        # Realizar la solicitud GET a la API de SUNAT
        response = requests.get(url)
        data = response.json()

        # Conectar a la base de datos SQLite
        conn = sqlite3.connect('base.db')
        cursor = conn.cursor()

        # Crear la tabla sunat_info si no existe
        cursor.execute('''CREATE TABLE IF NOT EXISTS sunat_info (
                            fecha TEXT PRIMARY KEY,
                            precio_compra REAL,
                            precio_venta REAL
                          )''')

        # Insertar los datos en la tabla sunat_info
        for registro in data:
            dolar_compra = registro['compra']
            dolar_venta = registro['venta']
            fecha = registro['fecha']
            cursor.execute("INSERT INTO sunat_info (fecha, precio_compra, precio_venta) VALUES (?, ?, ?)",
                           (fecha, dolar_compra, dolar_venta))
        
        # Guardar los cambios y cerrar la conexión
        conn.commit()
        conn.close()

    except requests.RequestException as e:
        print("Error al realizar la solicitud a la API de SUNAT:", e)

def mostrar_contenido_tabla():
    try:
        # Conectar a la base de datos SQLite
        conn = sqlite3.connect('base.db')
        cursor = conn.cursor()

        # Obtener y mostrar el contenido de la tabla sunat_info
        cursor.execute("SELECT * FROM sunat_info")
        rows = cursor.fetchall()
        for row in rows:
            print(row)

        # Cerrar la conexión
        conn.close()

    except sqlite3.Error as e:
        print("Error al acceder a la base de datos:", e)

# Obtener los datos de SUNAT y almacenarlos en la base de datos
obtener_datos_sunat()

# Mostrar el contenido de la tabla sunat_info
mostrar_contenido_tabla()
