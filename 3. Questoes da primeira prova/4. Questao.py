import os
import time
os.system("clear")

notasAluno = 4 
notas = []
nome = []
media = 0
soma = 0
contador = 0
resultado = 0

nome = input("Digite o nome do aluno: ")

for i in range(notasAluno):
    notas.append(input("Digite a iª nota:"))
    contador =+ 1 
    soma += notasAluno

media = soma / contador

if media >= 7:
    resultado = "Aprovado!"
elif media > 5 and media < 6.9:
    resultado = "Recuperação!"
else:
    resultado = "Reprovado!"

for i in range(notasAluno):
    print(notas[i+1])

print(f"Nome do aluno: {nome}")
print(f"Notas do aluno: {notasAluno[i]}")
print(f"Media: {media}")
print(f"Situação do aluno: {resultado}")