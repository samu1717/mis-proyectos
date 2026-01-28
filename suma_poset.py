import random
correcto = 0
for i in range(100):
    if correcto == 5:
        break
    numero = random.randint(1, 100)
    numero2 = random.randint(1, 100)

    respuesta = int(input(f"¿Cuánto es {numero} + {numero2}? "))
    suma = numero + numero2

    if respuesta == suma:
        correcto += 1
        print("Operaciones correctas:", correcto)
    else:
        print("Operación incorrecta")



