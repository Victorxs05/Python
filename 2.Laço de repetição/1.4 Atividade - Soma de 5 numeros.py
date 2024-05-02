import os

os.system("cls || clear")

#numeros = []
soma = 0
"""
(VETORES)
for i in range(5): 
    numeros.append(int(input(f"Digite o {i+1}º numero: ")))
    soma+=numeros[i]
    
    os.system("cls || clear")

for i in range(5):
    print(f"{i+1}º numero: {numeros[i]}")

print(soma)
"""

for i in range(1, 6):
    numeros = int(input(f"Digite o {i}º numero: "))
    soma += numeros

print(f"Soma: {soma}")