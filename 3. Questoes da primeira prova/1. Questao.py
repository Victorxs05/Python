import os
import time
os.system("clear")

numerosInteiros = 6
numeros = []
pares = 0
impares = 0 
contador = 0

for i in range(numerosInteiros):
    numeros.append(input(f"Digite um numero inteiro{i+1}:"))
    #numeros[i] += 1

if (numeros[i] % 2 == 0):
    pares += 1
else:
    impares += 1 


contador += 1 
for i in range(numerosInteiros):
    #numeros.append(input(f"Digite um numero inteiro{i+1}:"))
    print(numeros[i])

print(f"Numeros inseridos: {contador}")
print(f"Numeros pares: {pares}")
print(f"Numeros impares: {impares}")

    
