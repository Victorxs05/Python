import os 
import sys 
import time 

os.system("clear")

NUMEROS_INSERIDOS = 5 

numeros = []
maiorNumero = 0 
menorNumero = sys.maxsize


while True: 
    numero = int(input("Digite um numero: "))
    if numero == 0:
        break
    numeros.append(numero)


    maiorNumero = max(numeros)
    menorNumero = min(numeros)



print(f"Maior Numero: {maiorNumero}")
print(f"Menor Numero: {menorNumero}")