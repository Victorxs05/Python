import os
import time
os.system("clear")

num_alunos = 40
nomes = []
notas = []
media = 0

for i in range(num_alunos):
    nomes.append(input(f"Informe o do aluno {i+1}:"))
    notas.append(float(input(f"Informe a nota de {nomes[i]}:")))
    media += notas[i]

media = media / num_alunos
print(f"A media da turma é {media:.2f}")

for i in range(num_alunos):
    if notas[i] > media:
        print(f"Parabens {nomes[i]}!")