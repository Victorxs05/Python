import os 
from dataclasses import dataclass
os.system("cls || clear")

# Constante 
QUANTIDADE_ALUNOS = 2 

# Vetor
nomes = []
idades = []
alturas = []
pesos = []

# Classes
@dataclass
class Aluno:
    nome: str
    idade: int
    altura: float
    peso: int

alunos = []

# Solicitando dados para o usuário.
"""
for i in range(QUANTIDADE_ALUNOS):
    nome_do_aluno = input("Digite seu nome: ")
    idade_do_aluno = int(input("Digite sua idade: "))
    altura_do_aluno = float(input("Digite sua altura: "))
    peso_do_aluno = int(input("Digite seu peso: "))
    os.system("cls || clear")

    aluno = Aluno(nome = nome_do_aluno, idade = idade_do_aluno, altura = altura_do_aluno, peso = peso_do_aluno)
    alunos.append(aluno)
"""
for i in range(QUANTIDADE_ALUNOS):
    aluno = Aluno(
        nome = input("Digite seu nome: "),
        idade = int(input("Digite sua idade: ")),
        altura = float(input("Digite sua altura: ")),
        peso = int(input("Digite seu peso: "))
    )
    os.system("cls || clear")
    alunos.append(aluno)
# Exibindo dados para o usuário.
os.system("clear")
for i in alunos:
    print("=== EXIBINDO DADOS ALUNOS ===")
    print(f"Nome: {i.nome}")
    print(f"Idade: {i.idade}")
    print(f"Altura: {i.altura:.2f}")
    print(f"Peso: {i.peso}")