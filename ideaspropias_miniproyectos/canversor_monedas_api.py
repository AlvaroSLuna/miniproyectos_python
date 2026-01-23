# Voy a intentar sacar el conversor de monedas pero con api, lo mas probable es que tenga que usar copilot para que me explique como hacerlo

# Para llamar a la api necesitamos importar este directorio
import requests

# Tenemos que crear una funcion que de las tasas (llamando a la api) y otra funcion que convierta

def obtener_tasas(moneda_origen):

    """ 
    Llama a la API usando la moneda de origen.
    Devuelve un diccionario con las tasas de conversión.
    """
    url = f"https://api.exchangerate-api.com/v4/latest/{moneda_origen}"

    respuesta = requests.get(url) # Hacemos la petición GET 
    datos = respuesta.json() # Convertimos el JSON a diccionario 
    return datos["rates"] # Devolvemos solo las tasas

def convertir(moneda_origen, moneda_destino, cantidad):

    """ 
    Convierte una cantidad de una moneda a otra usando la API.
    """
    #Obtenemos las tasas desde la api
    tasas = obtener_tasas(moneda_origen)

    if moneda_destino not in tasas:
        # Esto de raise me lo ha dado la IA, entiendo que sera un print, pero que salte cuando da error al no estar la tasa puesta por el usuario
        raise ValueError('La moneda destino no existe en las tasas disponibles')
    
    tasa = tasas[moneda_destino]    # Se extrae la tasa concreta
    return cantidad * tasa          # Se realiza la conversion


# Ahora vamos con el programa principal

print ("*** Conversor de Monedas ***")

moneda_origen = input("\nMoneda de origen (EUR, USD, MXN, JPY, ...): ").upper()
moneda_destino = input("Moneda destino (EUR, USD, MXN, JPY, ...): ").upper()
cantidad = float(input("Cantidad a convertir: "))


resultado = convertir(moneda_origen, moneda_destino, cantidad)
print(f"\n{cantidad} {moneda_origen} equivalen a {resultado:.2f} {moneda_destino}")