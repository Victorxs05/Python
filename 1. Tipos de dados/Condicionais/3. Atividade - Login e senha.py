import os

os.system("cls || clear")

login: str  
senha: str 
#loginCadastrado: str = "Victor321" 
#senhaCadastrada: str = "senha123"

print("===Exibindo dados do usuario: ===")
login = input("Digite o login: ")
senha = input("Digite a senha: ")


if (login == "Victor321" and senha == "senha123"):
#if login == loginCadastrado and senha == senhaCadastrada:
    print("Bem-vindo!")
else : 
    print("Login ou senha inválidos.")



 
    