import os 
import time
import sys
os.system("clear")

class Livro:
    def _init_(self, titulo, autor, preco_compra, preco_aluguel, disponivel_compra=True, disponivel_aluguel=True):
        self.titulo = titulo
        self.autor = autor
        self.preco_compra = preco_compra
        self.preco_aluguel = preco_aluguel
        self.disponivel_compra = disponivel_compra
        self.disponivel_aluguel = disponivel_aluguel

# Lista de livros
livros = [
    Livro("Livro 1", "Autor 1", "50.0", "10.0"),
    Livro("Livro 2", "Autor 2", "45.0", "9.0"),
    Livro("Livro 3", "Autor 3", "40.0", "8.0"),
    Livro("Livro 4", "Autor 4", "55.0", "11.0"),
    Livro("Livro 5", "Autor 5", "60.0", "12.0"),
    Livro("Livro 6", "Autor 6", "35.0", "7.0")
]

def comprar_livro(titulo):
    for livro in livros:
        if livro.titulo == titulo:
            if livro.disponivel_compra:
                livro.disponivel_compra = False
                return f"Você comprou '{livro.titulo}' por R${livro.preco_compra:.2f}."
            else:
                return f"Desculpe, '{livro.titulo}' não está disponível para compra."
    return "Livro não encontrado."

def alugar_livro(titulo):
    for livro in livros:
        if livro.titulo == titulo:
            if livro.disponivel_aluguel:
                livro.disponivel_aluguel = False
                return f"Você alugou '{livro.titulo}' por R${livro.preco_aluguel:.2f}."
            else:
                return f"Desculpe, '{livro.titulo}' não está disponível para aluguel."
    return "Livro não encontrado."

def obter_informacoes_livro(titulo):
    for livro in livros:
        if livro.titulo == titulo:
            disponivel_compra = "Sim" if livro.disponivel_compra else "Não"
            disponivel_aluguel = "Sim" if livro.disponivel_aluguel else "Não"
            return (f"Título: {livro.titulo}\n"
                    f"Autor: {livro.autor}\n"
                    f"Preço de compra: R${livro.preco_compra:.2f}\n"
                    f"Preço de aluguel: R${livro.preco_aluguel:.2f}\n"
                    f"Disponível para compra: {disponivel_compra}\n"
                    f"Disponível para aluguel: {disponivel_aluguel}")
    return "Livro não encontrado."

# Exemplos de uso das funções
print(comprar_livro("Livro 1"))
print(alugar_livro("Livro 2"))
print(obter_informacoes_livro("Livro 3"))