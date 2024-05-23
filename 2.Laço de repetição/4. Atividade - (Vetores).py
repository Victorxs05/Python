import os 
import sys 
import time 

os.system("clear")

#Criando uma lista / vetor
notas = []

#Socilicitando 3 notas para o usuario
for i in range(3):
    nota = float(input("Digite uma nota: "))
    notas.append(nota)

#Exibindo as notas pára o usuario
for i in range(3):
    print(f"Nota: {notas[1]}")