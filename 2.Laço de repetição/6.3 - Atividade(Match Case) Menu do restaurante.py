import os 
import sys
os.system("cls || clear ")

while True: 
    print(f"=== MENU ===")
    print(f"Codigo |\t Prato            |\t Valor  ")
    print("\n")
    print(f"1      |\t Picanha          |\t R$ 25,00 \n")
    print(f"2      |\t Lasanha          |\t R$ 20,00 \n")
    print(f"3      |\t Strognoff        |\t R$ 18,00 \n")
    print(f"4      |\t Bife Acebolado   |\t R$ 15,00 \n")
    print(f"5      |\t Pão com ovo      |\t R$ 5,00 \n")
    opcao = int(input(f"Digite a opção desejada: "))

    os.system("clear")
    match(opcao):
        case 1: 
            opcao = "Picanha - R$ 25,00"
            break
        case 2: 
            opcao = "Lasanha -  R$ 20,00"
            break
        case 3: 
            opcao = "Strognoff - R$ 18,00"
            break
        case 4: 
            opcao = "Bife Acebolado - R$ 15,00"
            break
        case 5: 
            opcao = "Pão com ovo - R$ 5,00"
            break
        case _:
            print("Opção Invalida.")

if opcao:
    print(f"Prato: {opcao}")