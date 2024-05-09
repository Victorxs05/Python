import os
import time
import sys
os.system("clear")

mediaSalario = 0
somaSalario = 0
maiorIdade = 0
menorIdade = sys.maxsize
salarioMulheres = 0
idade = 0
contadorSalario = 0

while True: 

    print(f"=== MENU ===")
    print(f"Codigo |\t Descrição ")
    print(f"1 |\t Adicionar pessoa \n")
    print(f"2 |\t Exibir resultados e sair \n")
    opcao = int(input(f"Digite a opção desejada: "))

    match(opcao):
        case 1:
                while True: 
                    idade = int(input(f"Digite sua idade: "))
                    if (idade > 0):
                        break
                    else: 
                        print(f"Opção invalida. Tente novamente!")

                while True:  
                    sexo = input("Digite seu sexo(M ou F)")
                    sexo = sexo.upper()
                    if (sexo == "F" or sexo == "M"):
                        break
                    else: 
                        print(f"Opção invalida. Tente novamente!")

                while True:  
                    salario = float(input(f"Digite seu salario:"))
                    if (salario > 0):
                        break
                    else: 
                        print(f"Opção invalida. Tente novamente!")
                

                contadorSalario += 1
                somaSalario += salario
                mediaSalario = somaSalario / contadorSalario

                maiorIdade = max(idade, maiorIdade)
                menorIdade = min(idade, menorIdade)

                if (sexo == "F" and salario >= 5000):
                    salarioMulheres += 1
                if contadorSalario != 0:
                    mediaSalarios = somaSalario / contadorSalario

               
            


        case 2:
            print("=== Mostrando resultados ===")
            print(f"Média de salários do grupo: {mediaSalarios}")
            print(f"Maior idade do grupo: {maiorIdade}")
            print(f"Menor idade do grupo: {menorIdade}")
            print(f"Mulheres com salário a partir de 5 mil: {salarioMulheres}")
            break
        case _:
            print("Opção inválida. \nTente novamente.")

 




