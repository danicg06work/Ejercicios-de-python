# 23. Escribe un programa que pida un número al usuario y diga si es divisible por 3 y 5.
numero=float(input("Dime un numero: "))

if numero%3 ==0 and numero%5 != 0: 
    print("Es divisible por 3")
elif numero%5 == 0 and numero%3 != 0:
    print("Es divisible por 5")
elif numero%3 == 0 and numero%5 == 0:
    print("Es divisible tanto por 3 como por 5")
else:
    print("No es divisible ni por 3 ni por 5")
