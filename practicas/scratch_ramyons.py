# Porción del proyecto de Scratch traducida a Python
# Juego: recolectar ramyons para avanzar de nivel

nivel = 1
ramens = 0

while nivel <= 3:

    if nivel == 1:
        ramens_necesarios = 10
    elif nivel == 2:
        ramens_necesarios = 20
    else:
        ramens_necesarios = 30

    print("Nivel", nivel)
    print("Debes comer", ramens_necesarios, "ramyons.")

    while ramens < ramens_necesarios:
        ramens = ramens + 1
        print("Ramyons comidos:", ramens)

    print("¡Nivel completado!")

    nivel = nivel + 1
    ramens = 0

print("¡Ganaste!")
