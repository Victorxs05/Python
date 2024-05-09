import os

os.system("cls || clear")

while True:
    nota = float(input("Digite a nota(entre 0 e 10):"))

    if nota < 0 or nota > 10:
        print("Nota inválida. A nota deve estar entre 0 e 10. Por favor, tente novamente.")
    else:
        print("Nota válida:", nota)
        break