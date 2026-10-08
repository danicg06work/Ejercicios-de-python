# 24. Crea un programa que pida dos números al usuario e imprima el mayor de los dos.
n1 = float(input("Dime el numero1: "))
n2 = float(input("Dime el numero2: "))

if n1>n2:
    print("El numero",n1,"es mayor que el",n2)
elif n2>n1:
    print("El numero",n2,"es mayor que el numero",n1)
else:
    print("Ambos numeros son iguales") 