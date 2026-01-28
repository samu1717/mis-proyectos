lista = [7, 10, 3, 55]
maximo = lista[0]

for numero in lista:
    if numero > maximo:
        maximo = numero

print("El número más grande es:", maximo)
