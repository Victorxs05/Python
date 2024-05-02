import os

os.system("cls || clear")

nomeProduto: str
preco: float
desconto: float
quantidadeAdquirida: int
total = float
totalPagar: float

nomeProduto = input("Digite o nome do produto: ")
quantidadeAdquirida = float(input("Digite a quantidade: "))
preco = float(input("Preço do produto: "))

#total = quantidadeAdquirida * preco 

if quantidadeAdquirida <= 5:
    desconto = 0.02
elif quantidadeAdquirida <= 10:
    desconto = 0.03
else: 
    desconto = 0.05

totalPagar = preco - (preco * desconto)

"""
if quantidadeAdquirida <= 5:
    desconto = total - (total * 0.2)
elif quantidadeAdquirida <= 10:
    desconto = total - (total * 0.3)
else:
    desconto = total - (total * 0.5)
"""




print("===Exibindo resultados: ===")
print(f"Nome do produto: {nomeProduto}")
print(f"Quantidade Adquirida: {quantidadeAdquirida}")
print(f"Preço: {preco}")
print(f"Total a Pagar: {totalPagar}")
#print(f"Desconto: {desconto}")