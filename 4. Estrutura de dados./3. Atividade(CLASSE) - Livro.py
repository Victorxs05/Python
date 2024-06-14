import os 
from dataclasses import dataclass
os.system("cls || clear")

QUANTIDADE_LIVROS = 2

titulos = []
autores = []
numerosPaginas = []
precos = []

@dataclass
class Livro:
    titulo: str
    autor: str
    numeroPagina: int
    preco: float

livros = []

for i in range(QUANTIDADE_LIVROS):
    livrosB = Livro(
        titulo = input("Digite o nome do livro: "),
        autor = input("Digite o nome do autor: "),
        numeroPagina = int(input("Digite a quantidade de paginas: ")),
        preco = float(input("Digite o preço do livro:"))
    )
    os.system("cls || clear")
    livros.append(livrosB)

os.system("cls || clear")
for i in livros:
    print("=== EXIBINDO DADOS ===")
    print(f"Titulo: {i.titulo}")
    print(f"Autor: {i.autor}")
    print(f"Numeros de pagina: {i.numeroPagina}")
    print(f"Preço: {i.preco:.2f}")