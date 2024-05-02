import os

os.system("cls || clear")

numero: int

numero = int(input("Digite um numero: "))

for i in range(1, 11):
    print(f"Numero {i * numero}")
    #print(f"{numero} x {i} = {numero * i}")