# Voy a intentar crear una mini historia de aventuras, usando lo aprendido hasta ahora en el curso de udemy.
# Quiero utilizar el randint para crear decisiones aleatorias en la historia, intentando usar el if y else.
# Tambien quiero intentar probar el uso de switch, aunque no los he visto aun en el curso.

from random import randint

print("""Bienvenido a la pequeña aventura de Motsognir el enano guerrero.
      Tu papel en esta hostoria es ayudarle a tomar decisiones en su viaje.
      Cada decisión que tomes afectará el resultado de su aventura.""")


print("\nMotsognir llega a un cruce en el camino. ¿Debería ir a la izquierda hacia el bosque oscuro o a la derecha hacia las montañas nevadas?")
decision1 = input("Escribe 'izquierda' para el bosque o 'derecha' para las montañas: ").lower()
if decision1 == "izquierda":
    print("\nMotsognir decide ir hacia el bosque oscuro. Al entrar, se encuentra con un grupo de goblins que lo atacan.")
    accion1 = input("¿Debería luchar contra los goblins o intentar escapar? Escribe 'luchar' o 'escapar': ").lower()

    if accion1 == "luchar":
        print("\nMotsognir se prepara para sacar su arma y enfrentarse a los goblins.")
        arma1 = input("¿Qué arma debería usar? Escribe 'hacha' para su hacha de batalla o 'martillo' para su martillo de guerra: ").lower()
        goblins_salud = 10
        if arma1 == "hacha":
            fuerza_ataque = randint(1, 10) + 5  # Hacha tiene un bono de ataque
            print(f"Con su hacha, Motsognir ataca con una fuerza de {fuerza_ataque}.")

            if fuerza_ataque >= goblins_salud:
                print("\nMotsognir derrota a los goblins con su poderoso ataque.")
                print("\nMotsognir sale victorioso del combate, pero percibe que detras de los restos de los goblis logra discernir un cofre del tesoro." \
                " Abre el cofre y encuentra una gran cantidad de oro y joyas. ¡Ha tenido suerte en su aventura!" \
                " Motsognir decide irse del bosque y volver a su aldea para compartir su botín.")
                
            else:
                print(f"Los goblins resisten el ataque, les quedan {goblins_salud - fuerza_ataque} de salud restante.")
                print("\nLos goblins contraatacan, pero Motsognir lleva consigo un escudo, por el cual no recibe daño.")
                fuerza_ataque2 = randint(5, 10) + 5  # Hacha tiene un bono de ataque / Nuevo numero aleatorio para el segundo ataque, subo el daño para asegurar la victoria
                print(f"Despues del irrisorio ataque de los goblins, Motsognir derrota a los goblins propinandoles un ultimo golpe de {fuerza_ataque2}.")

                print("\nMotsognir sale victorioso del combate, pero percibe que detras de los restos de los goblis logra discernir un cofre del tesoro." \
                " Abre el cofre y encuentra una gran cantidad de oro y joyas. ¡Ha tenido suerte en su aventura!" \
                " Motsognir decide irse del bosque y volver a su aldea para compartir su botín.")
                
        elif arma1 == "martillo":
            fuerza_ataque = randint(1, 10) + 3  # Martillo tiene un bono de ataque menor
            print(f"Con su martillo, Motsognir ataca con una fuerza de {fuerza_ataque}.")

            if fuerza_ataque >= goblins_salud:
                print("\nMotsognir derrota a los goblins con su poderoso ataque.")
                print("\nMotsognir sale victorioso del combate, pero percibe que detras de los restos de los goblis logra discernir un cofre del tesoro." \
                " \nAbre el cofre y encuentra una gran cantidad de oro y joyas. ¡Ha tenido suerte en su aventura!" \
                " Motsognir decide irse del bosque y volver a su aldea para compartir su botín.")
                
            else:
                print(f"Los goblins resisten el ataque, les quedan {goblins_salud - fuerza_ataque} de salud restante.")
                print("\nLos goblins contraatacan, pero Motsognir por desgracia no lleva escudo, y es masacrado.")
                
    else:
        print("\nMotsognir intenta escapar, pero los goblins son rápidos y lo alcanzan.")
        print("Después de una breve lucha, Motsognir es capturado por los goblins y llevado a su guarida.")
        print("Allí, logra negociar su libertad ofreciendo parte de su botín futuro. Motsognir aprende a ser más cauteloso en sus aventuras.")

elif decision1 == "derecha":
    print("\nMotsognir decide ir hacia las montañas nevadas. Mientras avanza, una tormenta de nieve repentina lo sorprende.")