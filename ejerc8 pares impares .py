cantidad = int(input("¿Cuántos números vas a introducir? "))
pares = 0
impares = 0

for i in range(cantidad):
    num = int(input("Introduce un número: "))
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

print("Pares:", pares)
print("Impares:", impares)
