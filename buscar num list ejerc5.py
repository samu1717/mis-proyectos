lista = [30, 40, 50, 60, 70]
num = int(input("Introduce un número: "))
encontrado = 0

for numero in lista:
    if num == numero :
        encontrado = lista

if encontrado:
    print("El número está en la lista")
else:
    print("El número NO está en la lista")
