import os 
import sys 
import time 

os.system("clear")

#Criando uma constante 
QUANTIDADE_NOTAS = 3 

notas = []
#soma = 0
media = 0

#Solicitando 3 notas para o usuario:
for i in range(QUANTIDADE_NOTAS):
    nota = float(input("Digite uma nota: "))
    notas.append(nota)
    #soma += notas[i]

#media = soma / QUANTIDADE_NOTAS
media = sum(notas) / QUANTIDADE_NOTAS

#Exibindo as notas para o usuario:
os.system("clear")
for i in range(QUANTIDADE_NOTAS):
    print(f"Nota: {notas[i]}")

"""
# ForEach
for nota in notas:
    print(f"Nota: {nota}")
"""

print(f"Resultado da Media: {media}")