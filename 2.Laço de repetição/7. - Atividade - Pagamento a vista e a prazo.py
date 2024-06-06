import os 
import sys 
os.system("clear")
def logoSenai ():
    os.system("cls || clear")
    print("=== ============ ===")
    print("=== SENAI | FIEB ===")
    print("=== ============ ===")


produto = int(input("Digite o preço do produto: "))

while True:
    logoSenai ()
    print(f"1  - Pagamento à vista: ")
    print(f"2  - Pagamento à prazo: ")
    opcao = int(input("Digite a opção desejada: "))


 
    match(opcao):
        case 1: 
            #if opcao == 1:
                produto * 0.10
            #else: 
                break
        case 2: 
            #if opcao == 2: 
                print("Digite a quantidade de parcelas: ")

        
        case 1: 
            print("Valor do produto: R$ 100.00")
            print("Forma de pagamento: à vista.")
            print("Valor do desconto: R$ 10.00")
            print("Total a pagar: R$ 90.00")
            break
        case 2: 
            print("Valor do produto: R$ 100.00")
            print("Forma de pagamento: à prazo.")
            print("Quantidade de parcelas: 6")
            print("Valor do desconto: R$ 16.66")
            print("Total a pagar: R$ 100.00")
            break

if opcao: 
    print(f"Opção desejada: {opcao}")

if produto: 
    print(f"Valor do produto: {produto}")
