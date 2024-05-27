import os
import time
os.system("clear")

NOTAS_ALUNOS = 4 
notas = []
media = 0
soma = 0


nome = input("Digite o nome do aluno: ")

for i in range(NOTAS_ALUNOS):
    nota = int(input(f"Digite a {i+1}ª nota:"))
    notas.append(nota)
    soma += notas[i]

os.system("clear")
media = soma / NOTAS_ALUNOS
soma = 0

    
if media >= 7:
    resultado = "Aprovado!"
elif media > 5 and media < 6.9:
    resultado = "Recuperação!"
else:
    resultado = "Reprovado!"

for i in range(NOTAS_ALUNOS):
    print(f"{i+1}º nota: {notas[i]}")


print(f"Nome do aluno: {nome}")
print(f"Notas do aluno: {notas[i]}")
print(f"Media: {media}")
print(f"Situação do aluno: {resultado}")