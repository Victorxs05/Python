import os 
import sys
import time
from dataclasses import dataclass
def logoSenai ():
    os.system("cls || clear")
    print("=== SENAI === ")
    
def Inss(n1):
    if (n1 <= 1100): 
        resultadoInss = n1 * 0.075
    elif (n1 <= 2203.48):
        resultadoInss = n1 * 0.09
    elif (n1 <= 3305.22):
        resultadoInss = n1 * 0.12
    elif (n1 <= 6433.57):
        resultadoInss = n1 * 0.14
    else: 
        resultadoInss = 854.36
    return resultadoInss
    
def Irrf(n1):
    if (n1 <= 2259.2):
        resultadoIrrf = 0
    elif (n1 <= 2826.65):
        resultadoIrrf = n1 * 0.075
    elif (n1 <= 3751.05):
        resultadoIrrf = n1 * 0.15
    elif (n1 <= 4664.68):
        resultadoIrrf = n1 * 0.225
    else:
        resultadoIrrf = n1 * 0.275
    return resultadoIrrf    
    
def valeTransporte(n1):
    resultadoTransporte = n1 * 0.06
    return resultadoTransporte
    
def valeRefeicao(n1):
    resultadoRefeicao = n1 * 0.2
    return resultadoRefeicao
descontoTransporte = 0
valorDependentes = float
logoSenai ()
matricula = input("Digite sua matricula: ")
senha = int(input("Digite sua senha: "))
while True: 
    salarioBase = float(input("Digite seu salario base: "))
    if salarioBase < 1: 
        input("Tente novamente(PRESS ENTER): ")
    else: 
        break
    
while True: 
    dependentes = int(input("Digite a quantidade de dependentes: "))
    if (dependentes < 0 ):
        input("Tente Novamente(PRESS ENTER): ")
    else:
        valorDependentes = 189.59 * dependentes
        break
    
while True:
    transporteValor = input("Deseja receber valor de transporte? (Sim ou Não):")
    if (transporteValor == "Sim"):
        descontoTransporte = valeTransporte(salarioBase)
        break
    if (transporteValor == "Não"):
        break
    if (transporteValor != "Não" and transporteValor != "Sim"):
        input("Opção Invalida. Tente novamente(PRESS ENTER): ")
refeicaoValor = float(input("Digite o valor do vale refeição: "))

descontoInss = Inss(salarioBase)    
descontoIrrf = Irrf(salarioBase)
finalIrrf = descontoIrrf - valorDependentes
if finalIrrf < 0:
    finalIrrf = 0
descontoRefeicao = valeRefeicao(refeicaoValor)
calculo = descontoRefeicao + descontoTransporte + 150 + descontoInss + finalIrrf
salarioLiquido = salarioBase - calculo

print(f"Salário Bruto: {salarioBase}")
print(f"Salário Liquido: {salarioLiquido:.2f}")
print(f"Refeição: {descontoRefeicao}")










