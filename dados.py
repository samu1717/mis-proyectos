import random

print("Pulsa Enter para tirar los dados de cada jugador. Ctrl+C para terminar el juego.")

for ronda in range(1000000000):  

    suma = 0
    suma2 = 0

    
    input("Jugador 1, pulsa Enter para tirar los dados...")
    for jugador1 in range(6):  
        aleatorio = random.randint(1, 6)
        suma += aleatorio
        print("El valor del dado es:", aleatorio)
    print("La suma de los dados del jugador 1 es:", suma)

    # Turno del Jugador 2
    input("Jugador 2, pulsa Enter para tirar los dados...")
    for jugador2 in range(6):  
        aleatorio = random.randint(1, 6)
        suma2 += aleatorio
        print("El valor del dado es:", aleatorio)
    print("La suma de los dados del jugador 2 es:", suma2)

    if suma > suma2:
        print("Gana el jugador 1")
    elif suma == suma2:
        print("Empate")
    else:
        print("Gana el jugador 2")

    print("----------------------------")











