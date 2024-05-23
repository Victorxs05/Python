import os 
import sys 
import time 

os.system("clear")

NUMEROS_INSERIDOS = 6

numeros = []

pares = 0
impares = 0

for i in range(NUMEROS_INSERIDOS):
    numero = int(input(f"Digite um numero: "))
    numeros.append(numero)

    if numero % 2 == 0:
        pares += 1 
    else:
        impares += 1 


for i, numero in enumerate(numeros):
    print(f"{i+1}º numeros: {numero}")

print(f"Numeros pares: {pares}")
print(f"Numeros impares: {impares}")