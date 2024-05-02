import os

os.system("cls || clear")

nome: str
resultado : str
idade: int 
PrimeiraNota: float
SegundaNota: float
TerceiraNota: float 
media: float 

print("===Solicitando dados:===")
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
PrimeiraNota = float(input("Digite a primeira Nota: "))
SegundaNota = float(input("Digite a segunda Nota: "))
TerceiraNota = float(input("Digite a terceira Nota: "))

media = (PrimeiraNota + SegundaNota + TerceiraNota) / 3

if media >= 7:
    resultado = "Aprovado!"
if media < 5: 
    resultado = "Reprovado!"

print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Primeira nota: {PrimeiraNota}")
print(f"Segunda nota: {SegundaNota}")
print(f"Terceira nota: {TerceiraNota}")
print(f"Media: {media}")
print(f"Resultado: {resultado}")

# elif = else if 