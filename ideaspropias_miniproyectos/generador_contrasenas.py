# Al igual que hay con randint para numeros aleatorios, existe una libreria llamada 'secrets' que es usada para generar datos aleatorios seguros
# Asi que voy a usarla para crear un generador de contraseñas segura, usando letras mayusculas, minusculas, numeros y simbolos
# La idea es que puedas pedir una longitud de contraseña de X a Y caracteres y el programa genere una contraseña segura de esa longitud
# La longitu minima va a ser de 8 caracteres y la maxima de 32 caracteres para asegurar una buena seguridad

import secrets
# No sabia de la existencia de esta libreria, pero investigando un poco encontre que existe una libreria llamada 'string' que tiene varios grupos de caracteres predefinidos
# Asi que la voy a usar para facilitar la creacion de la contraseña
import string

def token_generator(length):

    # Definimos los conjuntos de caracteres a usar, incluyendo simbolos especiales
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = "!@#$%^&*()-_=+[]{}|;:,.<>?/"

    # Combinamos todos los caracteres en un solo conjunto
    all_chars = lowercase + uppercase + digits + symbols

    # Con este metodo nos aseguramos de que la contraseña tenga al menos un caracter de cada tipo
    password = [
        secrets.choice(lowercase),
        secrets.choice(uppercase),
        secrets.choice(digits),
        secrets.choice(symbols)
    ]

    # Rellenamos el resto de la contraseña con caracteres aleatorios del conjunto completo
    # El += es un operador que extiende la lista existente, en lugar de crear una nueva
    password += [secrets.choice(all_chars) for _ in range(length - 4)]

    # Mezclamos la lista para evitar un patrón predecible
    secrets.SystemRandom().shuffle(password)

    return ''.join(password)


# Solicitamos al usuario la longitud deseada para la contraseña
min_length = 8
max_length = 32

# Y manejamos posibles errores en la entrada del usuario, usando un bloque try-except
# Esto hace que el programa no se caiga si el usuario ingresa algo incorrecto
try:
    length = int(input(f"Ingrese la longitud deseada para la contraseña ({min_length}-{max_length}): "))
    
    if min_length <= length <= max_length:
        generated_password = token_generator(length)
        print(f"Contraseña generada: {generated_password}")
    else:
        print(f"Error: La longitud debe estar entre {min_length} y {max_length} caracteres.")

except ValueError:
    print("Error: Debe ingresar un número válido.")
