import os

os.system("cls || clear")

PrimeiroNumero : float  
SegundoNumero : float
soma: float
subt: float
multi: float
div: float

PrimeiroNumero = float(input("Digite o primeiro numero: "))
SegundoNumero = float(input("Digite o segundo numero: "))

soma = PrimeiroNumero + SegundoNumero
subt = PrimeiroNumero - SegundoNumero
multi = PrimeiroNumero * SegundoNumero
div = PrimeiroNumero / SegundoNumero

print(f"Primeiro Numero: {PrimeiroNumero}")
print(f"Segundo Numero: {SegundoNumero}")
print(f"Soma: {soma}")
print(f"Subtracao: {subt}")
print(f"Multiplicacao: {multi}")
print(f"Divisao: {div}")

