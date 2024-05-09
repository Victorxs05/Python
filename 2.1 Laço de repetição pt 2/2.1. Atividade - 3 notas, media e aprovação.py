import os

os.system("cls || clear")

soma = 0 
media = 0 

for i in range(1, 4): 
    numeros = int(input(f"Digite a {i}ª nota: "))
    soma += numeros
    media = soma / 3


if (media >= 7):
    print(f"Aprovado!")
if (media > 4 and media < 7):
    print(f"Recuperação!")
if (media < 4):
    print(f"Reprovado!")

print(f"Media : {media}")