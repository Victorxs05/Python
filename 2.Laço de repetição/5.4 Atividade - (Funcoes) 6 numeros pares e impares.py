import os 
os.system("clear")



def logoSenai ():
    os.system("cls || clear")
    print("=== ============ ===")
    print("=== SENAI | FIEB ===")
    print("=== ============ ===")

def numeros_pares(numeros):
    pares = 0
    for numero in numeros:
        if numero % 2 == 0:
            pares += 1 
    return pares 
  
def numeros_impares(numeros):
    impares = 0
    for numero in numeros:
        if numero % 2 != 0:
            impares += 1 
    return impares 

NUMEROS_INSERIDOS = 6 

lista_numeros = []

logoSenai ()
for i in range(NUMEROS_INSERIDOS):
    numero = int(input("Digite um número: "))
    lista_numeros.append(numero)

quantidadePares = numeros_pares(lista_numeros)
quantidadeImpares = numeros_impares(lista_numeros)

logoSenai ()
print(f"Quantidade de pares: {quantidadePares}")
print(f"Quantidade de impares: {quantidadeImpares}")
    
    

