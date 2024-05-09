import os
import time
os.system("clear")

contador = 0
soma = 0
while True: 
    valor = int(input("Digite um valor positivo: "))

    if valor > 0:
        valor = int(input("Digite um valor positivo: "))
        soma += valor
        contador += 1 
    if valor < 0:
        break

media = soma / contador
print(f"Media: {media}")