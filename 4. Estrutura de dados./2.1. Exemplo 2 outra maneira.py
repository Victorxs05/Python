import os 

os.system("cls || clear")

class Aluno:
    def __init__(self, nome_qualquer: str, idade_qualquer:int):
        self.nome = nome_qualquer
        self.idade = idade_qualquer

QUANTIDADE_ALUNOS = 2 
alunos = []

for i in range(QUANTIDADE_ALUNOS):
    nome_usuario = input("Digite seu nome: ")
    idade_usuario = int(input("Digite sua idade: "))
    alunos.append(Aluno(nome_usuario, idade_usuario))

for i in alunos:
    print("=== EXIBINDO DADOS ALUNOS ===")
    print(f"Nome: {i.nome}")
    print(f"Idade: {i.idade}")
