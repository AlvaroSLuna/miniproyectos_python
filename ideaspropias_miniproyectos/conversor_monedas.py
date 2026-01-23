# Vamos a hacer un conversor de monedas al no usar una api la cual me de las tasas actualizadas, debo generar un diccionario con las tasas para poder practicar

# Le pedimos al usuario la moneda actual (la que quiere convertir) y la moneda a la cual quiere convertir. Y despues le pedimos la cantidad
moneda_actual = input(f"Que moneda quieres convertir? (EUR, USD, MXN, JPY): ")
cantidad_moneda = float(input(f"Ingresa la cantidad a convertir: "))
moneda_convertir = input(f"A que moneda quieres convertir? (EUR, USD, MXN, JPY): ")


tasas = {
    ("EUR", "USD"): 1.10,
    ("USD", "EUR"): 0.90,

    ("EUR", "MXN"): 18.50,
    ("MXN", "EUR"): 0.054,

    ("EUR", "JPY"): 160.0,
    ("JPY", "EUR"): 0.0062,

    ("USD", "MXN"): 16.80,
    ("MXN", "USD"): 0.059,

    ("USD", "JPY"): 145.0,
    ("JPY", "USD"): 0.0069,

    ("MXN", "JPY"): 8.60,
    ("JPY", "MXN"): 0.116
}



try:

    tasa = tasas[(moneda_actual, moneda_convertir)]
    moneda_convertida = cantidad_moneda * tasa

    print(f"Sus {cantidad_moneda} en {moneda_actual} son {moneda_convertida} en {moneda_convertir}")

# Ponemos KeyError y ValueError para manejar los errores en caso de que el usuario ingrese una moneda no valida o intente convertir una moneda a si misma
except (KeyError, ValueError):

    print("Introduce un valor correcto / No puedes convertir una moneda a su misma moneda.")