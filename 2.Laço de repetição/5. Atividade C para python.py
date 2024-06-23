import os
import sys
import time 
notas = []
TAM = 3
os.system("cls || clear")

def calcular_media(notas):
    for i in range(TAM):
        soma = 0
        soma += notas[i]
    return soma / TAM

def verificarSituacao(media):
    if media >= 7:
        resultado = "Aprovado!"
    else:
        resultado = "Reprovado!"
    return resultado

def mostrar_resultado(notas):
    print(f"\nMédia: {calcular_media(notas):.1f}")
    print(f"Resultado: {verificarSituacao(calcular_media)}")


for i in range(TAM):
    nota = float(input(f"Digite a {i + 1}ª nota: "))
    notas.append(nota)

#print(f"Resultado: {mostrar_resultado(notas)}")
resultado = mostrar_resultado(notas)
media = calcular_media(notas)

