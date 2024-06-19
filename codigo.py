import os
import math
from dataclasses import dataclass
def logoSenai():
    os.system("cls || clear")
    print("=== SENAI === ")

def calcular_imc(peso, altura):
   return peso / math.pow(altura, 2)

def situacaoIMC(imc):
    if imc < 18.5 :
        resultado = "Muito magro"
    elif imc < 25:
        resultado = "Peso normal"
    elif imc < 30:
        resultado = "Sobrepeso"
    elif imc < 35:
        resultado = "Obesidade grau I"
    elif imc < 40:
        resultado = "Obesidade grau II"
    else:
        resultado = "Obesidade grau III (mórbida)"

    return resultado

class DadosUsuario:
    def __init__(self, nome_usuario: str, sobrenome_usuario: str, nomeCompletos: str, idade_usuario, altura_usuario, peso_usuario, imcs_usuario, resultados_usuario):
        self.nome = nome_usuario
        self.sobrenome = sobrenome_usuario
        self.nomeCompletos = nome_usuario + sobrenome_usuario
        self.idade = idade_usuario
        self.altura = altura_usuario
        self.peso = peso_usuario
        self.imcs = imc
        self.situacaoIMC = situacao
        
        
dadosDosUsuarios = []
nomeCompletos = str

while True:
    logoSenai()
    nome_usuario = input("Digite o nome do usuário (ou digite 'sair' para encerrar): ")
    if nome_usuario.lower() == 'sair':
        break
    sobrenome_usuario = input("Digite o sobrenome do usuário: ")
    idade_usuario = int(input("Digite a idade do usuário: "))
    altura_usuario = float(input("Digite a altura do usuário (em metros): "))
    peso_usuario = float(input("Digite o peso do usuário (em quilogramas): "))
    imc = calcular_imc(peso_usuario, altura_usuario)
    situacao = situacaoIMC(imc)
    
    dadosDosUsuarios.append(DadosUsuario(nome_usuario, sobrenome_usuario, nomeCompletos, idade_usuario, altura_usuario, peso_usuario, imc, situacao))    
    
logoSenai()
print("\nDados dos usuários: \n")
for j,i  in enumerate(dadosDosUsuarios):
    print(f"Usuário {j+1}")
    print(f"Nome: {i.nome}")
    print(f"Sobrenome: {i.sobrenome}")
    print(f"Nome completo: {i.nomeCompletos}")
    print(f"Idade: {i.idade}")
    print(f"Altura:{i.altura} metros")
    print(f"Peso: {i.peso} quilogramas")
    print(f"IMC: {i.imcs:.1f}")
    print(f"Situação: {i.situacaoIMC}")
    print()








