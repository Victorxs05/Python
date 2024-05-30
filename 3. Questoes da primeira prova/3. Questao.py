import os
import time
os.system("clear")


nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
email = input("Digite seu e-mail: ")
telefone = int(input("Digite seu telefone: "))

while True: 
    print("=== MENU ===")
    print("1 | \t Mostrar nome e idade: \n ")
    print("2 | \t Mostrar nome e e-mail: \n ")
    print("3 | \t Mostrar nome e telefone: \n ")
    print("4 | \t Mostrar todas as informações: \n ")
    print("0 | \t Sair do programa: \n ")
    opcao = int(input(f"Digite a opção desejada:"))
    os.system("clear")
    match(opcao):
        case 1: 
            print(nome)
            print(idade)
            break
        case 2: 
            print(nome)
            print(email)
            break
        case 3:
            print(nome)
            print(telefone)
            break
        case 4:
            print(nome)
            print(idade)
            print(email)
            print(telefone)
            break
        case _:
            os.system("clear")
            input("Opção incorreta, tente novamente.")
            print("=== MENU ===")
            print("1 | \t Mostrar nome e idade: \n ")
            print("2 | \t Mostrar nome e e-mail: \n ")
            print("3 | \t Mostrar nome e telefone: \n ")
            print("4 | \t Mostrar todas as informações: \n ")
            print("0 | \t Sair do programa: \n ")

            if opcao == 0:
                break
            else: 
                print("=== MENU ===")
                print("1 | \t Mostrar nome e idade: \n ")
                print("2 | \t Mostrar nome e e-mail: \n ")
                print("3 | \t Mostrar nome e telefone: \n ")
                print("4 | \t Mostrar todas as informações: \n ")
                print("0 | \t Sair do programa: \n ")
print("\n")
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"E-mail: {email}")
print(f"Telefone: {telefone}")

#if opcao:
    #print(f"Opção: {opcao}")
