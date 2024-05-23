import os 

# Função sem retorno.

def logoSenai ():
    os.system("cls || clear")
    print("=== ===== ===")
    print("=== SENAI ===")
    print("=== ===== ===")

# Função com retorno.

def somar(n1,n2):
    resultado = n1 + n2
    return resultado

#Solicitando dados para o usuario;
logoSenai ()
nome = input("Digite seu nome: ")

logoSenai ()
idade = int(input("Digite sua idade: "))

logoSenai ()
peso = float(input("Digite seu peso: "))

# Exibindo dados para o usuario.

logoSenai ()
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Peso: {peso:.2f}")