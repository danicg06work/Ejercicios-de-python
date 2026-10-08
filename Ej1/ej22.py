# 22. Crea un programa que verifique si una persona es mayor de edad o menor de edad, considerando 18 años como mayoría de edad.
edad=int(input("Dime la edad para decirte si eres mayor de edad: "))

if edad>18 or edad==18:
    print("Es mayor de edad")
else:
    print("Eres menor")