import os

# Função sem retorno.
def logoSenai():
    os.system("cls || clear")
    print("=== SENAI === ")

def imc(n1,n2):
    imc = n1 / (n2 * n2)
    print(f"IMC: {imc: .1f}")
    
    if imc < 18.5: 
        print("IMC: Abaixo do peso.")
    if imc >= 18.5 and imc < 25:
        print("IMC: Peso normal.")
    if imc >= 25 and imc < 30:
        print("IMC: Sobrepeso.")
    if imc >= 30 and imc < 35:
        print("IMC: Obesidade grau I.")
    if imc >= 35 and imc < 40:
        print("IMC: Obesidade grau II.")
    if imc >= 40:
        print("IMC: Obesidade grau III.")

# Definindo listas vazias para armazenar os dados dos usuários
nomes = []
sobrenomes = []
idades = []
alturas = []
pesos = []

# Solicitando os dados dos usuários em um loop
while True:
    logoSenai()
    nome = input("Digite o nome do usuário (ou digite 'sair' para encerrar): ")
    if nome.lower() == 'sair':
        break
    sobrenome = input("Digite o sobrenome do usuário: ")
    
    # Verificando se o usuário quer sair
    
    idade = int(input("Digite a idade do usuário: "))
    altura = float(input("Digite a altura do usuário (em metros): "))
    peso = float(input("Digite o peso do usuário (em quilogramas): "))
    
    # Adicionando os dados às listas
    nomes.append(nome)
    sobrenomes.append(sobrenome)
    idades.append(idade)
    alturas.append(altura)
    pesos.append(peso)
    

# Exibindo os dados armazenados
logoSenai()
print("\nDados dos usuários:")
for i in range(len(nomes)):
    print(f"=== Usuário {i+1}=== :")
    print("Nome:", nomes[i], sobrenomes[i])
    print("Idade:", idades[i])
    print("Altura:", alturas[i], "metros")
    print("Peso:", pesos[i], "quilogramas")
    imc(pesos[i], alturas[i])