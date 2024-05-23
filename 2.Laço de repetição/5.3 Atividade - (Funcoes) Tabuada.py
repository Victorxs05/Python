import os 

def logoSenai ():
    os.system("cls || clear")
    print("=== ===== ===")
    print("=== SENAI ===")
    print("=== ===== ===")

def tabuada(numero): 
    for i in range(10):
        print(f"{numero} x {i+1} = {numero * {i+1}}")

logoSenai ()
numero = int(input("Digite um numero: "))


tabuada(numero)

#print(f"Numero informado: {numero}")
#print(f"Tabuada: {tabuada}")

    
