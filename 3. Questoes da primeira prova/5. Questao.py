import os
import time
import sys
os.system("clear")

numeroInteiros: int = 5
numero = 0
contador = 0
maiorNumero = 0
menorNumero = 999

#for i in range(numeroInteiros):
for i in range(numeroInteiros):
    numero = int(input(f"Digite o {i+1}º numero: "))
    contador += 1 
    if numero > maiorNumero:
        maiorNumero = numero
    if numero < menorNumero:
        menorNumero = numero
#maiorNumero = max(numero, maiorNumero)
#menorNumero = min(numero, menorNumero)

print(f"Numeros inseridos: {contador}")
print(f"Maior Numero: {maiorNumero}")
print(f"Menor Numero: {menorNumero}")