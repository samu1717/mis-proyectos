cantidad = int(input("¿Cuántos números vas a introducir? "))
suma = 0

for i in range(cantidad):
    num = float(input("Introduce un número: "))
    suma += num

print("La suma total es:", suma)
