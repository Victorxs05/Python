import os
import sys
import time 
TAM = 3
notas = []
def calcularMedia(n1,n2):
    soma = 0
    for i in range(TAM):
        soma += notas[i]
    return soma / TAM

def verificarSituacao(media):
    if media >= 7:
        resultado = "Aprovado!"
    else:
        resultado = "Reprovado!"
    return resultado

def mostrarResultado(notas):
    print(f"\nMédia: {calcularMedia:.1f}")
    print(f"Resultado: {verificarSituacao},{calcularMedia}, {notas}")

for i in range(TAM):
    print(f"Digite a {i+1}ª nota: {i}")
    notas.append()



