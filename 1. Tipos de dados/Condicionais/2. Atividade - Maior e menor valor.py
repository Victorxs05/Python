import os

os.system("cls || clear")

PrimeiroNumero: int
SegundoNumero: int
media: float
soma: float
multi: float
MenorValor: float
MaiorValor: float

print("===Solicitando dados: ===")
PrimeiroNumero =  float(input("Digite o primeiro numero: "))
SegundoNumero =  float(input("Digite o segundo numero: "))

media = (PrimeiroNumero + SegundoNumero) / 2 
soma = PrimeiroNumero + SegundoNumero
multi = PrimeiroNumero * SegundoNumero

MaiorValor = max(PrimeiroNumero, SegundoNumero)
MenorValor = min(PrimeiroNumero, SegundoNumero)

"""
if PrimeiroNumero > SegundoNumero:
    MaiorValor = PrimeiroNumero
    MenorValor = SegundoNumero
else : 
    MaiorValor = SegundoNumero
    MenorValor = PrimeiroNumero
"""

print(f"Primeiro Numero: {PrimeiroNumero}")
print(f"Segundo Numero: {SegundoNumero}")
print(f"Media: {media}")
print(f"Soma: {soma}")
print(f"Multiplicação: {multi}")
print(f"Maior Valor: {MaiorValor}")
print(f"Menor Valor: {MenorValor}")
