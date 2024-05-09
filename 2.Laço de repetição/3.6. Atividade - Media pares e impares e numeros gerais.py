import os
import time
os.system("clear")

contador = 0
pares = 0
impares = 0
mediaPares = 0
numeros = int 
soma = 0
somaPares = 0

while True: 
    numeros = int(input("Digite um numero positivo: "))
    if numeros > 0:
        numeros = int(input("Digite um numero positivo: "))
        soma += numeros
    if numeros == 0:
        break
    if (numeros % 2 == 0):
        pares += 1 
        somaPares += numeros
    if (numeros % 2 == 1):
        impares += 1 

contador += 1 
mediaPares = somaPares / pares
media = soma / contador

print(f"\n")
print(f"Media dos numeros pares: {mediaPares}")
print(f"Quantidade de numeros pares: {somaPares}")
print(f"Media Geral: {media}")


