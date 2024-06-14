import os 
os.system("cls || clear")

# Constante 
QUANTIDADE_ALUNOS = 2 

# Vetor
nomes = []
idades = []

# Solicitando dados para o usuário.
for i in range(QUANTIDADE_ALUNOS):
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))

    nomes.append(nome)
    idades.append(idade)

# Exibindo dados para o usuário.
os.system("clear")
for i in range(QUANTIDADE_ALUNOS):
    print(f"Nome: {nomes[i]}")
    print(f"Idade: {idades[i]}")