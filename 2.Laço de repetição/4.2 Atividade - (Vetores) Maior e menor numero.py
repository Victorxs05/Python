import os 
import sys 
import time 

os.system("clear")

NUMEROS_INSERIDOS = 5 

numeros = []
maiorNumero = 0 
menorNumero = sys.maxsize

for i in range(NUMEROS_INSERIDOS):
    numero = int(input("Digite um numero: "))
    numeros.append(numero)
os.system("clear")

maiorNumero = max(numeros)
menorNumero = min(numeros)

for i, numero in enumerate(numeros):
    print(f"{i+1}º Numeros: {numero}")


print(f"Maior Numero: {maiorNumero}")
print(f"Menor Numero: {menorNumero}")


