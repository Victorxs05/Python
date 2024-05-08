import os

os.system("cls || clear")

QUANTIDADE_NOTAS = 3
soma = 0

for i in range(QUANTIDADE_NOTAS):
    while True:
        nota = float(input(f"Digite a {i+1}ª nota(entre 0 e 10): "))

        if nota < 0 or nota > 10:
            print("Nota inválida: Por favor, tente novamente. \n")
        else: 
            soma += nota
            break

media = soma / QUANTIDADE_NOTAS
if (media >= 7):
    resultado = "Aprovado"
if (media > 5 and media < 6.9):
    resultado ="Recuperação"
if (media < 5):
    resultado = "Reprovado"

print(f"Média: {media}")
print(f"Situação do aluno: {resultado}")