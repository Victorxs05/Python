import os 
from dataclasses import dataclass
os.system("cls || clear")

QUANTIDADE_PET = 2

nomes = []
idades = []
racas = []
portes = []
alimentacoes = []

@dataclass
class Pet:
    nome:str
    idade:int
    raca:str
    porte:str
    alimentacao:str

pets = []

for i in range(QUANTIDADE_PET):
    petss = Pet(
        nome = input("Digite o nome do pet: "),
        idade = int(input("Digite a idade do pet: ")),
        raca = input("Digite a raça do pet: "),
        porte = input("Digite o porte: "),
        alimentacao = input("Digite a alimentação do pet: ")
    )
    os.system("cls || clear")
    pets.append(petss)

os.system("cls || clear")
for i in pets:
    print("=== EXIBINDO DADOS ===")
    print(f"Nome do pet: {i.nome}")
    print(f"Idade do pet: {i.idade}")
    print(f"Raça do pet: {i.raca}")
    print(f"Porte: {i.porte}")
    print(f"Alimentação do pet: {i.alimentacao}")
