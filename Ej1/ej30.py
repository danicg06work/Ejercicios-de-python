# 30. Escribe un programa que pida al usuario un número y luego imprima todos los números del 1 hasta ese número.
numero = float(input("Dime un numero"))
contador = 1
if numero >= 1:
    while contador<=numero:
        print(contador)
        contador+=1
elif numero < 1:
    while contador >= numero:
        print(contador)
        contador-=1
