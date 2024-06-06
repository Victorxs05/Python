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
    opcao = int(input("Digite um numero de mês do ano: "))

    match(opcao):
        case 1: 
            opcao = "Janeiro"        
            break
        case 2:
            opcao = "Fevereiro"        
            break
        case 3: 
            opcao = "Março"        
            break
        case 4: 
            opcao = "Abril"        
            break
        case 5: 
            opcao = "Maio"        
            break
        case 6: 
            opcao = "Junho"        
            break
        case 7: 
            opcao = "Julho"        
            break
        case 8: 
            opcao = "Agosto"        
            break
        case 9: 
            opcao = "Setembro"        
            break
        case 10: 
            opcao = "Outubro"
            break
        case 11: 
            opcao = "Novembro"
            break   
        case 12: 
            opcao = "Dezembro"
            break
        case _:
            input("Mês invalido. Tente novamente: ")
         

if opcao:
    print(f"Mês do ano: {opcao}")