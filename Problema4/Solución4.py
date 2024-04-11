import requests
url= "https://api.coindesk.com/v1/bpi/currentprice.json"
response = requests.get(url)
data = response.json()
bitcoin_price_dolar = data["bpi"]["USD"]["rate"]
bitcoin_price_libra = data["bpi"]["GBP"]["rate"]
bitcoin_price_euro = data["bpi"]["EUR"]["rate"]

# Escribir los datos en un archivo de texto local
with open("precio_bitcoin.txt", "w") as file:
    file.write(f"Precio de Bitcoin en USD: {bitcoin_price_dolar}\n")
    file.write(f"Precio de Bitcoin en GBP: {bitcoin_price_libra}\n")
    file.write(f"Precio de Bitcoin en EUR: {bitcoin_price_euro}\n")

print("Datos de precios de Bitcoin almacenados en el archivo 'precio_bitcoin.txt'")

