import os 
import sys 
os.system("clear")

prato = []
subtotal = 0
totalPagar = 0
desconto = 0
parcela = 0
quantidadeParcelas = 0
contador = 0


while True: 
    os.system("clear")
    print(f"\t      ======== MENU ========")
    print(f"Codigo      |\t Prato                |\t Valor" )
    print(f"1           |\t Pizza de calabresa   |\t R$ 35,00 \n")
    print(f"2           |\t Pizza de 4 queijos   |\t R$ 30,00 \n")
    print(f"3           |\t Pizza de frango      |\t R$ 32,00 \n")
    print(f"4           |\t Macarronada          |\t R$ 25,00 \n")
    print(f"5           |\t Lasanha              |\t R$ 20,00 \n")
    print(f"6           |\t Strognoff            |\t R$ 18,00 \n")
    print(f"7           |\t Açai                 |\t R$ 15,00 \n")
    opcao = int(input("Digite a opção desejada: "))
    match(opcao):
        case 1:
            prato.append("Pizza de calabresa - R$ 35,00")
            subtotal += 35
            contador += 1
        case 2:
            prato.append("Pizza de queijo - R$ 30,00")
            subtotal += 30
            contador += 1
        
        case 3:
            prato.append("Pizza de frango - R$ 32,90")
            subtotal += 32
            contador += 1
   
        case 4:
            prato.append("Macarronada - R$ 25,00")
            subtotal += 25
            contador += 1
       
        case 5:
            prato.append("Lasanha - R$ 20,00")
            subtotal += 20
            contador += 1
       
        case 6:
            subtotal += 18
            prato.append("Strognoff - R$ 18,00")
            contador += 1
            
        case 7:
            prato.append("Açai - R$ 15,00")
            subtotal += 15
            contador += 1
            
        case 0:
            break
        case _:
            print("Opção Invalida. Tente novamente:\n ")
            
    if opcao >= 0 and opcao < 8:
        repetirPrato = int(input("Deseja adicionar mais um prato? ( 1 - Sim | 0 - Não ) : "))
        if repetirPrato != 1 and repetirPrato != 0:
            input("Opção invalida. Tente novamente. ")
            repetirPrato = int(input("Deseja adicionar mais um prato? ( 1 - Sim | 0 - Não ) : "))
        if (repetirPrato == 0):
            break        
while True:    
    formaPagamento = int(input("Escolha a forma de pagamento: ( 1 - À vista | 2 - À prazo)  "))
    if formaPagamento != 1 and formaPagamento != 2:
        input("Opção invalida. Tente novamente. ")
    if formaPagamento == 1 or formaPagamento == 2:
        break
        
if (formaPagamento == 1):
        desconto = subtotal * 0.1
        totalPagar = subtotal - desconto
        print(f"Desconto: {desconto}")
        print(f"Subtotal: {subtotal}")
        print(f"Total a pagar: {totalPagar}")
       
if (formaPagamento == 2):
        taxa = subtotal * 0.10
        totalPagar = subtotal + taxa 
        print(f"Subtotal: {subtotal}")
        print(f"Acréscimo: {taxa}")
        print(f"Total a pagar: {totalPagar}")
        
            
        
        

    
    
            

    

