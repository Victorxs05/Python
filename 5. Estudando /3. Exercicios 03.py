import os 
os.system("cls || clear")

n = input("Digite algo: ")

print('O tipo primitivo desse valor é', type(n))
print("Só tem espaco? ",n.isspace())
print("É um número? ",n.isnumeric())
print("É alfabético? ",n.isalpha())
print("Está em maiúsculas? ",n.isupper())
print("Está em minúscula? ",n.islower())
print("Está capitalizada?",n.istitle())