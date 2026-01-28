#Juego de dados entre dos jugadores
import random
suma=0
suma2=0
for jugador1 in range (6):
    aleatorio=random.randint(1,6)
    suma+=aleatorio
    print("El valor del dado es:",aleatorio)
print("La suma de los dados es jugador1 es :",suma)
for jugador2 in range (6):
    aleatorio=random.randint(1,6)
    suma2+=aleatorio
    print("El valor del dado es:",aleatorio)
print("La suma de los dados es del jugador2 es :",suma2)
if suma>suma2:
    print("Gana el jugador 1")
elif suma==suma2:
    print("Empate")
else:
    print("Gana el jugador 2")





