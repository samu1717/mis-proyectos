cantidad = int(input("¿Cuántos números vas a introducir? "))
negativos = 0

for i in range(cantidad):
    num = int(input("Introduce un número: "))
    if num < 0:
        negativos += 1

print("Números negativos:", negativos)
