import requests

def precio_bitcoin():
    try:
        # Solicitar al usuario la cantidad de bitcoins que posee
        bitcoins = float(input("Ingrese la cantidad de bitcoins que posee: "))
        
        # Consultar la API del índice de precios de Bitcoin de CoinDesk
        url = "https://api.coindesk.com/v1/bpi/currentprice.json"
        response = requests.get(url)
        data = response.json()
        
        # Obtener el precio actual de Bitcoin en dolar
        dolar_precio = data["bpi"]["USD"]["rate_float"]
        
        # Calcular el costo actual de los bitcoins en dolar
        dolar_costo = bitcoins * dolar_precio
        
        # Mostrar el costo actual de los bitcoins en dolar con cuatro decimales y formato de miles
        print(f"El costo actual de {bitcoins} bitcoins es: ${dolar_costo:,.4f}")
    
    except ValueError:
        print("Error: Por favor ingrese un número válido de bitcoins.")
    except requests.RequestException as p:
        print(f"Error al conectarse a la API de CoinDesk: {p}")
    except KeyError:
        print("Error: No se pudo obtener el precio actual de Bitcoin.")
    except Exception as p:
        print(f"Error inesperado: {p}")

# Obtener el precio de Bitcoin
precio_bitcoin()
