import os
import time
os.system("clear")

numeros: int 
soma = 0
contador = 0


while True:
    numeros = int(input("Digite um numero positivo:"))
    if numeros >= 0:
        contador += 1
        soma += numeros
    elif numeros < 0: 
        break

media = soma / contador 

print(f"Numeros positivos: {contador}")
print(f"Media: {media}")