import os 

#Limpar terminal;
os.system("cls || clear")

#Inicializar variavel
resultado = False 

#while (resultado == 0):
while True:
    os.system("clear")
#Solicitar dados para o usuario
    a = int(input("Digite o primeiro numero: "))
    operador = input("Digite o operador: + - * / : ")
    b = int(input("Digite o segundo numero: "))
    match(operador):
        case '+':
            resultado = a + b
            break
        case '-':
            resultado = a - b
            break
        case '*':
            resultado = a * b
            break
        case '/':
            resultado = a / b
            break
        case _:
            os.system("clear")
            input("Operador invalido.")
            #operador = input("Digite o operador: ")


if resultado: 
    print(f"Resultado: {resultado}")