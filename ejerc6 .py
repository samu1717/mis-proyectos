cantidad = int(input("¿Cuántos números vas a introducir? "))

primer = int(input("Introduce el primer número: "))

for i in range(cantidad - 1):
    num = int(input("Introduce un número: "))
    if num <= primer:
        print("Este número no es mayor que el primero")
