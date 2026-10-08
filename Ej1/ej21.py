# 21. Escribe un programa que verifique si un número es positivo, negativo o cero, e imprima el mensaje correspondiente.
numero=float(input("Dime un numero para decirte de que tipo es: "))

if numero>0:
    print("Es positivo")
elif numero==0:
    print("El numero es 0")
else:
    print("El numero es negativo")