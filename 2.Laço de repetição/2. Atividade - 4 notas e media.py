import os
<<<<<<< HEAD
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
=======

os.system("cls || clear")

soma = 0 
media = 0 

for i in range(1, 5): 
    numeros = int(input(f"Digite a {i}ª nota: "))
    soma += numeros
    media = soma / 4

print(f"Media : {media}")
>>>>>>> c891460 (Aula 4)
