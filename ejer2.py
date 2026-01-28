num = int(input("Introduce un número entero: "))
num1=int(input("Introduce un número entero: "))
for i in range(num ,num1+1):
    if i % 2 == 0:
        print(i, "es un número par")
    else:
        print(i, "es un número impar")
