import os 
import sys
os.system("clear")
nome = str
matricula = int
opcaoAluguel =  int
opcao = int
contador = 0 
def menuLivro():
    os.system("clear")
    print(f"\t      ======== MENU ========")
    print(f"Codigo      |\t Livro                |\t Valor" )
    print(f"1           |\t Grande Principe      |\t R$ 75,00 \n")
    print(f"2           |\t Pequeno Principe     |\t R$ 60,00 \n")
    print(f"3           |\t Bela e a Fera        |\t R$ 59,90 \n")
    print(f"4           |\t Os Simpsons          |\t R$ 80,00 \n")
    print(f"5           |\t Ben 10               |\t R$ 10,00 \n")
    print(f"6           |\t Bob Esponja          |\t R$ 45,00 \n")

def comprarLivros(opcao):
    opcao = int("Digite a opcao desejada: ")
    match(opcao): 
        case 1: 
            resultadoEscolha = ("Grande Principe \n - Autor: Emilio Rosa \n - Paginas: 200 \n - R$ 75,00")
            contador += 1 
        case 2: 
            resultadoEscolha = ("Pequeno Principe \n - Autor: Antoine de Saint \n - Paginas: 100 \n - R$ 60,00")
            contador += 1 
        case 3: 
            resultadoEscolha = ("A Bela e a Fera \n - Autor: Gabrielle-Suzanne \n - Paginas: 208 \n - R$ 59,90")
            contador += 1 
        case 4: 
            resultadoEscolha = ("Os Simpsons \n - Autor: Matt Groening \n - Paginas: 500 \n - R$ 80,00")
            contador += 1 
        case 5: 
            resultadoEscolha = ("Ben 10 \n - Autor: Joe Kelly \n - Paginas: 357 \n - R$ 10,00")
            contador += 1 
        case 6: 
            resultadoEscolha = ("Bob Esponja \n - Autor: Stephen Hillenburg \n - Paginas: 242 \n - R$ 45,00")
            contador += 1 
        case _:
            print("Opção Invalida:")
    return resultadoEscolha


def alugarLivros(opcaoAluguel):
    while True:
        opcaoAluguel = int(input("Deseja alugar um livro? (Sim - 1 | Não - 0) "))
        if opcaoAluguel == 1:
            opcaoAluguel = int("Digite a opcao desejada: ")
            match(opcaoAluguel): 
                case 1: 
                    aluguelEscolha = ("Grande Principe \n - Autor: Emilio Rosa \n - Paginas: 200 \n - R$ 35,00 \n - Prazo de Entrega: 15 dias")
                case 2: 
                    aluguelEscolha =("Pequeno Principe \n - Autor: Antoine de Saint \n - Paginas: 100 \n - R$ 30,00 \n - Prazo de Entrega: 15 dias")
                case 3: 
                    aluguelEscolha = ("A Bela e a Fera \n - Autor: Gabrielle-Suzanne \n - Paginas: 208 \n - R$ 24,90 \n - Prazo de Entrega: 15 dias")
                case 4: 
                    aluguelEscolha = ("Os Simpsons \n - Autor: Matt Groening \n - Paginas: 500 \n - R$ 40,00 \n - Prazo de Entrega: 15 dias")
                case 5: 
                    aluguelEscolha = ("Ben 10 \n - Autor: Joe Kelly \n - Paginas: 357 \n - R$ 5,90 \n - Prazo de Entrega: 15 dias")
                case 6: 
                    aluguelEscolha = ("Bob Esponja \n - Autor: Stephen Hillenburg \n - Paginas: 242 \n - R$ 22,50 \n - Prazo de Entrega: 15 dias")
                case _:
                    print("Opção Invalida:")
            return aluguelEscolha
        if opcaoAluguel >= 0 and opcaoAluguel < 6:  
            if opcaoAluguel != 1 and opcaoAluguel != 0:
                print("Opcão invalida!")
                opcaoAluguel = int(input("Deseja alugar um livro? (Sim - 1 | Não - 0) "))
            if opcaoAluguel == 0:
                break

nome = input("Digite seu nome: ")
matricula = int(input("Digite sua matricula: "))

compraDeLivros = comprarLivros(resultadoEscolha)
alugar_livro = alugarLivros(opcaoAluguel)

print(f"Quantidade de Livros escolhidos: {contador}")
print(f"Nome do Leitor: {nome}")
print(f"Matricula do usuario: {matricula}")


      
    
