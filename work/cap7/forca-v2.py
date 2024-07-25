# Import
import random
from os import system, name

# Limpando a tela
def limpa_tela():
    # Windows
    if name == 'nt':
        _= system('cls')
    # Mac ou Linux
    else:
        _= system('clear')

# Função
def game():
    limpa_tela()
    print("\nBem vindo(a) ao jogo da forca versão 2!")
    print("Adivinhe a palavra abaixo:\n")

    # Lista de palavras para o jogo
    palavras = ['renegade','compass','ram','pegeout','argo']

    # Escolhe randomicamente uma palavra
    palavra = random.choice(palavras)

    # Lista de letras da palavra
    lista_letras_palavras = [letra for letra in palavra]

    # Cria o tabuleiro com o caracter "_" multiplicado pelo comprimento da palavra
    tabuleiro = ["_"] * len(palavra)

    # Número de chances
    chances = 6

    # Lista para letras digitadas
    letras_tentativas = []

    # Loop enquanto o número de chnaces for maior do que zero
    while chances > 0:
        print(display_hangman(chances))
        print("Palavra: ", tabuleiro)
        print("\n")

        # Tentativa
        tentativa = input("\nDigite uma letra: ")