# 25. Escribe un programa que determine si un número es divisible entre 2, entre 3 o entre ambos.
numero=float(input("Dime un numero: "))

if numero%2 ==0 and numero%3 != 0: 
    print("Es divisible por 2")
elif numero%3 == 0 and numero%2 != 0:
    print("Es divisible por 3")
elif numero%2 == 0 and numero%3 == 0:
    print("Es divisible tanto por 2 como por 3")
else:
    print("No es divisible ni por 2 ni por 3")