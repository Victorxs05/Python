import os 
import sys 
os.system("cls || clear")

numero = int 
resultado = False 
numero = int(input("Digite um numero (1 a 7): "))

match(numero):
    case 1: 
        resultado = "Domingo"
        print("Final de semana")
    case 2:
        resultado = "Segunda"
        print("Dia útil")
    case 3:
        resultado = "Terça-Feira"
        print("Dia útil")
    case 4:
        resultado = "Quarta-Feira"
        print("Dia útil")
    case 5: 
        resultado = "Quinta-Feira"
        print("Dia útil")
    case 6: 
        resultado = "Sexta-Feira"
        print("Dia útil")
    case 7:
        resultado = "Sabado"
        print("Final de semana")
    case _:
        print("Invalido.")

if resultado: 
    print(f"Dia da semana: {resultado}")