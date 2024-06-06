import os 
import sys 
os.system("clear")
def logoSenai ():
    os.system("cls || clear")
    print("=== ============ ===")
    print("=== SENAI | FIEB ===")
    print("=== ============ ===")

while True: 
    logoSenai ()
    produto = int(input("Digite o preço do produto: "))

    print(f"1  - Pagamento à vista: ")
    print(f"2  - Pagamento à prazo: ")
    opcao = int(input("Digite a opção desejada: "))

    match(opcao): 
        case 1: 
            desconto = produto * 0.1
            precoFinal = produto - desconto
            print(f"Valor do produto:{produto}")
            print("Forma de pagamento: à vista.")
            print(f"Valor do desconto: {desconto}")
            print(f"Total a pagar: {precoFinal}")
            break
        case 2: 
            parcela = int(input("Digite a quantidade de parcelas: "))
            precoParcela = produto / parcela
            print(f"Valor do produto: {produto}")
            print("Forma de pagamento: à prazo.")
            print(f"Quantidade de parcelas: {parcela} ")
            print(f"Valor por parcela: {precoParcela:.1f}")
            print(f"Total a pagar: {produto}")
            break
        case _: 
            print("Opção invalida: \n")



