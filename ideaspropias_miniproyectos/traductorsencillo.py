# He visto que puedo instalar una biblioteca de python el cual sirve de traductor
# Para instalarlo ponemos en la terminal pip install googletrans

# Entonces vamos a pedirle al usuario que frase quiere traducir y a que idioma y se lo pasamos automaticamente

import asyncio
from googletrans import Translator
print("""\n Ya que el idioma es en japones te pongo un listado con los mas hablados y que te sea sencillo ponerlo:\n
          * Español = es
          * Inglés = en
          * Chino mandarín = zh-cn
          * Hindi = hi
          * Portugués = pt
          * Árabe = ar
          * Ruso = ru
          * Japonés = ja
          """)
async def traducir():

    # Pedimos al usuario la frase y el idioma al que quiere traducir
    frase_traducir = input(f'*** Bienvenido al traductor ***\n\nIntroduce la frase que quieras traducir: ')
    #El idioma puede ser cualquiera pero tiene que ser en formato codigo en ingles.
    idioma = input(f'Introduce el idioma al que quieras traducir "en = Ingles": ')

    traductor = Translator()

    frase_traducida = await traductor.translate(frase_traducir, dest=idioma)

    print((f"Aqui tienes tu frase traducida: {frase_traducida.text}"))

asyncio.run(traducir())

# He tenido que ver que son las funciones asincronas para que el traductor funcione correctamente, ya que si no lo hacia de esta manera me daba error
# Basicamente una funcion asincrona es una funcion que puede pausar su ejecucion para esperar a que se complete una tarea que toma tiempo, y luego reanudar su ejecucion
# Ponemos el await antes de llamar a la funcion de traduccion para indicarle que espere a que se complete esa tarea antes de continuar

# El asyncio.run(traducir()) es la forma de ejecutar la funcion asincrona principal en un programa de python, siendo sincero aqui he tenido que pedir
# ayuda a copilot para que me explicara como hacerlo, ya que no tenia mucha idea de como funcionaba esto de las funciones asincronas en python