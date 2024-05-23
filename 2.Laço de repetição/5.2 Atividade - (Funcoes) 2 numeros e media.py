import os 

def logoSenai ():
    os.system("cls || clear")
    print("=== ===== ===")
    print("=== SENAI ===")
    print("=== ===== ===")

def somar(n1,n2):
    return n1 + n2
def media(n1,n2):
    return (n1 + n2) / 2


logoSenai ()
primeiroNumero = int(input("Digite o primeiro número: "))
logoSenai ()
segundoNumero = int(input("Digite o segundo número: "))

soma = somar(primeiroNumero, segundoNumero)
mediaNumeros = media(primeiroNumero, segundoNumero) 

print(f"Soma: {soma}")
print(f"Media: {mediaNumeros}")

