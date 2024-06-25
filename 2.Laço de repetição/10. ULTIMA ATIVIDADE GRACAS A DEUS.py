import os 
import sys 
os.system("cls || clear")

livros = []
preco = 0
contador = 0

while True: 
    os.system("clear")
    print(f"\t      ======== MENU ========")
    print(f"Codigo      |\t Livro                |\t Valor" )
    print(f"1           |\t Pequeno Principe     |\t R$ 35,00 \n")
    print(f"2           |\t Grande Principe      |\t R$ 30,00 \n")
    print(f"3           |\t Bela e a Fera        |\t R$ 32,00 \n")
    print(f"4           |\t Os Simpsons          |\t R$ 25,00 \n")
    print(f"5           |\t Ben 10               |\t R$ 20,00 \n")
    print(f"6           |\t Bob Esponja          |\t R$ 18,00 \n")
    opcao = int(input("Digite a opção desejada: "))
    match(opcao):
        case 1:
            resultado = ("Pequeno Principe \n - Autor: Antoine de Saint \n - Paginas: 100 \n - R$ 35,00")
            livros.append("Pequeno Principe \n - Autor: Antoine de Saint \n - Paginas: 100 \n - R$ 35,00")
            preco += 35
            contador += 1
        case 2:
            livros.append("Grande Principe \n - Autor: Emilio Rosa \n - Paginas: 200 \n - R$ 30,00")
            livros.append("Grande Principe - R$ 30,00")
            preco += 30
            contador += 1
        
        case 3:
            livros.append("Bela e a Fera \n - Autor: Gabrielle-Suzanne \n - Paginas: 208 R$ 32,90")
            preco += 32
            contador += 1
   
        case 4:
            livros.append("Os Simpsons  - R$ 25,00")
            preco += 25
            contador += 1
       
        case 5:
            resultado = "Ben 10 - R$ 20,00"
            livros.append("Ben 10 - R$ 20,00")
            preco += 20
            contador += 1
       
        case 6:
            resultado = "Bob Esponja - R$ 18,00"
            livros.append("Bob Esponja - R$ 18,00")
            preco += 18
            contador += 1
            
        case 0:
            break
        case _:
            print("Opção Invalida. Tente novamente:\n ")
         
    if opcao >= 0 and opcao < 8:
        adicionarLivro = int(input("Deseja comprar mais um livro? ( 1 - Sim | 0 - Não ) : "))
    if adicionarLivro != 1 and adicionarLivro != 0:
            input("Opção invalida. Tente novamente. ")
            adicionarLivro = int(input("Deseja comprar mais um livro? ( 1 - Sim | 0 - Não ) : "))
    if (adicionarLivro == 0):
            break   
            
print(f"Total a pagar: {preco}") 
print(f"Livro: {resultado}")  
print(f"Livro: {contador}")  