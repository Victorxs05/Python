import os

os.system("cls || clear")

nome: str 
sexo: str 
estadoCivil: str 
tempoCasada: int 

nome = input("Digite seu nome: ")
sexo = input("Digite seu sexo (M ou F): ")
estadoCivil = input("Digite seu estado civil: ")

sexo = sexo.lower()
estadoCivil = estadoCivil.lower()

if (sexo == "f" and estadoCivil == "casada"):
    tempoCasada = input("Digite quantos anos casada: ")
 

print(f"Nome:{nome}")
print(f"Sexo:{sexo}")
print(f"Estado Civil:{estadoCivil}")
print(f"Tempo de casada:{tempoCasada}")

