def calcular_media(notas):
    soma = sum(notas)
    return soma / len(notas)

def verificar_situacao(media):
    return "Aprovado!" if media >= 7 else "Reprovado!"

def mostrar_resultado(notas):
    media = calcular_media(notas)
    print(f"\nMédia: {media:.1f}")
    print(f"Resultado: {verificar_situacao(media)}")

def main():
    notas = []
    
    for i in range(3):
        nota = float(input(f"Digite a {i + 1}ª nota: "))
        notas.append(nota)
    
    mostrar_resultado(notas)

if __name__ == "__main__":
    main()
