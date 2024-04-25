import os

os.system("cls || clear")

kgMorango: float
kgMaca: float
precoMorango: float
precoMaca: float
precoTotal: float
desconto: float
precoFinal: float

kgMorango = float(input("Digite a quantidade de morangos em kg:"))
kgMaca = float(input("Digite a quantidade de maçã em kg: "))

if kgMorango <= 5:
    precoMorango = kgMorango * 2.50
else:
    precoMorango = kgMorango * 2.20
if kgMaca <= 5:
    precoMaca = kgMaca * 1.80
else: 
    precoMaca = kgMaca * 1.50

precoTotal = precoMorango + precoMaca

if kgMorango + precoMaca > 8 or precoTotal > 25:
    desconto = precoTotal * 0.1
    precoFinal = precoTotal - desconto
else: 
    print("OK!")


print(f"Quantidade de Morangos: {kgMorango}")
#print(f"Preço Morango: {precoMorango}")
print(f"Quantidade de Maçã: {kgMaca}")
#print(f"Preço Maçã: {precoMaca}")
print(f"Desconto: {desconto}")
print(f"Preço Total: {precoTotal}")