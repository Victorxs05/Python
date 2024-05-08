import os

os.system("cls || clear")

soma = 0 
media = 0 

for i in range(1, 5): 
    numeros = int(input(f"Digite a {i}ª nota: "))
    soma += numeros
    media = soma / 4

print(f"Media : {media}")