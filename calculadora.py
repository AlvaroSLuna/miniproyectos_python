# Voy a intentar crear una calculadora simple, usando lo aprendido hasta ahora en el curso de udemy
# Aun no he dado los condicionales, pero quiero intentar hacer algo simple

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
operacion = input("Ingrese la operación (+, -, *, /): ")

# Realizar la operación según la entrada del usuario
# En python se usa 'elif' para condiciones múltiples, similar a 'else if' en otros lenguajes
# También se usa ':' para indicar el inicio de un bloque de código
# Dentro de cada if o elif tambien puede haber mas condicionales

if operacion == "+":
    resultado = num1 + num2
    print(f"El resultado de {num1} + {num2} es: {resultado}")
elif operacion == "-":
    resultado = num1 - num2
    print(f"El resultado de {num1} - {num2} es: {resultado}")
elif operacion == "*":
    resultado = num1 * num2
    print(f"El resultado de {num1} * {num2} es: {resultado}")
elif operacion == "/":
    # Manejar la división por cero
    if num2 != 0:
        resultado = num1 / num2
        print(f"El resultado de {num1} / {num2} es: {resultado}")
    else:
        print("Error: No se puede dividir por cero.")
else:
    # Manejamos que el digito añadido no sea valido
    print("Operación no válida. Por favor ingrese +, -, * o /.")