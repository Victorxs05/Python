import os


os.system("cls || clear")
contadorNotas = 0
soma = 0 


while True: 
    nota = int(input("Digite uma nota: "))

    print("S - Inserir mais uma nota: \t")
    print("P - Ver quantas notas foram inseridas: \t")
    print("N - Calcular a média artmétrica das notas informadas: \t")
    resposta = input(f"Deseja mais uma nota?")

    # Converter o texto digitado em maiúsculo
    resposta = resposta.upper()

    contadorNotas += 1 
    soma += nota
    
    if resposta == "S":
         nota = int(input("Digite mais uma nota: "))        
    if resposta == "P":
         print(f"Quantidade de notas inseridas: {contadorNotas}")
    if resposta == "N":
         media = soma / contadorNotas
    break


media = soma / contadorNotas

print(f"Média: {media}")