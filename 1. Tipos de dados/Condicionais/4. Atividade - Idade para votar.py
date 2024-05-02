import os

os.system("cls || clear")

nome: str
idade: int 

print("===Exibindo resultados: ===")
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

if idade >= 18 and idade < 65:
    print("São obrigados a votar.")
else:
    print("NÃO são obrigados a votar.")

print(f"Nome:{nome}")
print(f"Idade:{idade}")
