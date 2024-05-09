import os

os.system("cls || clear")
contadorNotas = 0
soma = 0 


while True: 
    nota = int(input("Digite uma nota: "))
    resposta = input(f"Deseja mais uma nota?")

    # Converter o texto digitado em maiúsculo
    resposta = resposta.upper()

    contadorNotas += 1 
    soma += nota
    
    if resposta != "N": 
        break


media = soma / contadorNotas

print(f"Média: {media}")
print(f"Quantidade de loops: {contadorNotas}")