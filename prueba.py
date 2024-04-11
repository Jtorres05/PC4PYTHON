import requests
import sqlite3
from datetime import datetime

def obtener_precio_bitcoin():
    # Consultar la API de Bitcoin para obtener los precios en USD, GBP y EUR
    bitcoin_api_url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    response = requests.get(bitcoin_api_url)
    data = response.json()
    precios = data["bpi"]

    # Consultar la API de SUNAT para obtener el tipo de cambio PEN
    sunat_api_url = "https://api.apis.net.pe/v1/tipo-cambio-sunat"
    response_sunat = requests.get(sunat_api_url)
    data_sunat = response_sunat.json()
    tipo_cambio_pen = data_sunat["compra"]

    # Calcular el precio de compra de 10 bitcoins en PEN y EUR
    precio_bitcoin_usd = precios["USD"]["rate_float"]
    precio_bitcoin_gbp = precios["GBP"]["rate_float"]
    precio_bitcoin_eur = precios["EUR"]["rate_float"]
    precio_compra_10_btc_pen = 10 * precio_bitcoin_usd * tipo_cambio_pen
    precio_compra_10_btc_eur = 10 * precio_bitcoin_eur
    precio_compra_10_btc_eur = 10 * precio_bitcoin_gbp

    return precio_compra_10_btc_pen, precio_compra_10_btc_eur

def almacenar_datos(precio_compra_10_btc_pen, precio_compra_10_btc_eur):
    # Conectar a la base de datos SQLite
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()

    # Crear la tabla bitcoin si no existe
    cursor.execute('''CREATE TABLE IF NOT EXISTS bitcoin (
                        fecha TEXT PRIMARY KEY,
                        precio_compra_10_btc_pen REAL,
                        precio_compra_10_btc_eur REAL
                      )''')

    # Obtener la fecha actual
    fecha_actual = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Insertar los datos en la tabla bitcoin
    cursor.execute("INSERT INTO bitcoin (fecha, precio_compra_10_btc_pen, precio_compra_10_btc_eur) VALUES (?, ?, ?)",
                   (fecha_actual, precio_compra_10_btc_pen, precio_compra_10_btc_eur))
    
    # Guardar los cambios y cerrar la conexión
    conn.commit()
    conn.close()

def consultar_datos():
    # Conectar a la base de datos SQLite
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()

    # Consultar la base de datos para obtener el precio de compra de 10 bitcoins en PEN y EUR
    cursor.execute("SELECT * FROM bitcoin")
    rows = cursor.fetchall()
    for row in rows:
        print("Fecha:", row[0])
        print("Precio de compra de 10 bitcoins en PEN:", row[1])
        print("Precio de compra de 10 bitcoins en EUR:", row[2])

    # Cerrar la conexión
    conn.close()

# Obtener el precio de compra de 10 bitcoins en PEN y EUR
precio_compra_10_btc_pen, precio_compra_10_btc_eur = obtener_precio_bitcoin()

# Almacenar los datos en la base de datos
almacenar_datos(precio_compra_10_btc_pen, precio_compra_10_btc_eur)

# Consultar los datos almacenados en la base de datos
consultar_datos()
