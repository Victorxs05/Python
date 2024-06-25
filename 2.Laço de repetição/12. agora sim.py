import os
import sys
import time
os.system("cls || clear")


def menu_livro():
    #os.system("cls || clear")
    print(f"\t      ======== MENU ========")
    print(f"Codigo      |\t Livro                |\t Valor")
    print(f"1           |\t Grande Principe      |\t R$ 75,00 \n")
    print(f"2           |\t Pequeno Principe     |\t R$ 60,00 \n")
    print(f"3           |\t A Bela e a Fera      |\t R$ 59,90 \n")
    print(f"4           |\t Os Simpsons          |\t R$ 80,00 \n")
    print(f"5           |\t Ben 10               |\t R$ 10,00 \n")
    print(f"6           |\t Bob Esponja          |\t R$ 45,00 \n")

def comprar_livros():
    opcao = int(input("Digite a opcao desejada: "))
    contador = 0
    resultado_escolha = ""
    match(opcao):
        case 1:
            resultado_escolha = "Grande Principe \n - Autor: Emilio Rosa \n - Paginas: 200 \n - R$ 75,00"
            contador += 1
        case 2:
            resultado_escolha = "Pequeno Principe \n - Autor: Antoine de Saint \n - Paginas: 100 \n - R$ 60,00"
            contador += 1
        case 3:
            resultado_escolha = "A Bela e a Fera \n - Autor: Gabrielle-Suzanne \n - Paginas: 208 \n - R$ 59,90"
            contador += 1
        case 4:
            resultado_escolha = "Os Simpsons \n - Autor: Matt Groening \n - Paginas: 500 \n - R$ 80,00"
            contador += 1
        case 5:
            resultado_escolha = "Ben 10 \n - Autor: Joe Kelly \n - Paginas: 357 \n - R$ 10,00"
            contador += 1
        case 6:
            resultado_escolha = "Bob Esponja \n - Autor: Stephen Hillenburg \n - Paginas: 242 \n - R$ 45,00"
            contador += 1
        case _:
            print("Opção Inválida")
        
            return resultado_escolha, contador

def alugar_livros():
    aluguel_escolha = ""
    
    while True:
        opcao_aluguel = int(input("Deseja alugar um livro? (Sim - 1 | Não - 0) "))
        
        if opcao_aluguel == 1:
            opcao_aluguel = int(input("Digite a opcao desejada: "))
            match(opcao_aluguel):
                case 1:
                    aluguel_escolha = "Grande Principe \n - Autor: Emilio Rosa \n - Paginas: 200 \n - R$ 35,00 \n - Prazo de Entrega: 15 dias"
                case 2:
                    aluguel_escolha = "Pequeno Principe \n - Autor: Antoine de Saint \n - Paginas: 100 \n - R$ 30,00 \n - Prazo de Entrega: 15 dias"
                case 3:
                    aluguel_escolha = "A Bela e a Fera \n - Autor: Gabrielle-Suzanne \n - Paginas: 208 \n - R$ 24,90 \n - Prazo de Entrega: 15 dias"
                case 4:
                    aluguel_escolha = "Os Simpsons \n - Autor: Matt Groening \n - Paginas: 500 \n - R$ 40,00 \n - Prazo de Entrega: 15 dias"
                case 5:
                    aluguel_escolha = "Ben 10 \n - Autor: Joe Kelly \n - Paginas: 357 \n - R$ 5,90 \n - Prazo de Entrega: 15 dias"
                case 6:
                    aluguel_escolha = "Bob Esponja \n - Autor: Stephen Hillenburg \n - Paginas: 242 \n - R$ 22,50 \n - Prazo de Entrega: 15 dias"
                case _:
                    print("Opção Inválida")
                    return aluguel_escolha
        
        elif opcao_aluguel == 0:
            break
        else:
            print("Opcão invalida!")

def exibir_quantidade_livros():
    quantidade_livros = 6
    print(f"A quantidade de livros disponíveis é: {quantidade_livros}")

nome = input("Digite seu nome: ")
matricula = int(input("Digite sua matricula: "))

#os.system("cls || clear")
menu_livro()
compra_de_livros, contador = comprar_livros()
alugar_livro = alugar_livros()

os.system("clear")
opcao_quantidade = int(input("Deseja saber a quantidade de livros disponíveis? (Sim - 1 | Não - 0):  "))
if opcao_quantidade == 1:
    exibir_quantidade_livros()

print(f"Quantidade de Livros escolhidos: {contador}")
print(f"Nome do Leitor: {nome}")
print(f"Matricula do usuario: {matricula}")

if compra_de_livros:
    print(f"Compra de Livros:\n{compra_de_livros}")
if alugar_livro:
    print(f"Aluguel de Livros:\n{alugar_livro}")