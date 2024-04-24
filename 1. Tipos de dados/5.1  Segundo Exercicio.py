import os

os.system("cls || clear")

nome: str
idade: int
PrimeiraNota: float
SegundaNota: float
media: float

print("===Solicitando Dados:===")
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
PrimeiraNota = float(input("Digite a primeira Nota: "))
SegundaNota = float(input("Digite a segunda Nota:"))

media = (PrimeiraNota + SegundaNota) / 2 

print(f"Nome: {nome}")
print(f"idade: {idade}")
print(f"Primeiro Nota: {PrimeiraNota}")
print(f"Primeiro Nota: {SegundaNota}")
print(f"Media: {media}")