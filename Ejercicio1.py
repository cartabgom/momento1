#1. Construir un programa que permita ingresar 20 números enteros y
#   cuente cuantos números negativos fueron ingresados (+1)
print("Contar los números enteros y números negativos")
contador = 1
numNegativos = 0

while (contador<=20):
    num = int(input(f'Digite el número {contador}: '))

    if(num<0):
        numNegativos+=1
    
    contador+=1

print(f'{numNegativos} son numeros negativos')
