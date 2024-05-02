import os

os.system("cls || clear")

pares = 0
impares = 0

for i in range(1, 6): 
    numeros = int(input(f"Digite o {i}º numero: "))
for i in range(1, 6): 
    if ( i % 2 == 0):
        print(f"Numeros pares: {i}")

for i in range(1, 6): 
    if ( i % 2 != 0): 
        print(f"Numeros impares: {i}")

#print(f"Numeros pares: {pares}")
#print(f"Numeros impares: {impares}")
