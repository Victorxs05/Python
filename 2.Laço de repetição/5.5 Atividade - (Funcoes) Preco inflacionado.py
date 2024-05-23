import os 
os.system("clear")

def logoSenai ():
    os.system("cls || clear")
    print("=== ============ ===")
    print("=== SENAI | FIEB ===")
    print("=== ============ ===")

def inflacionar(precoProduto): 
    if precoProduto < 100:
        precoProduto * 0.10
    else: 
        precoProduto * 0.20
    


logoSenai ()
precoProduto = float(input("Digite o preço do produto: "))

inflacionar(precoProduto)

print(f"Produto: {precoProduto}")



