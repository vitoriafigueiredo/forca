print('*******************************')
print('Seja bem vindo ao jogo da forca')
print('*******************************')

from random import choice

with open('palavras.txt') as arquivo:
 linhas = arquivo.read()
 listas_de_palavras = linhas.split('\n')

 palavra = choice(listas_de_palavras).upper()

acertos = 0
erros = 0
tentativas_total = 0
letras_acertadas = ''
letras_erradas = ''
ganhou = True

while (tentativas_total == 0):

    print("Qual o nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Selecione sua dificuldade: "))

    if(nivel == 1):
        tentativas_total = 20
    elif(nivel == 2):
        tentativas_total = 10
    elif(nivel == 3):
        tentativas_total = 6
    else:
        tentativas_total = 0
        print("Digite um número válido")


while acertos != len(palavra) and erros != tentativas_total:
 letra = input('Digite a letra: ').upper()

 if letra in palavra:
    print('Você acertou a letra!!')
    letras_acertadas += letra
    acertos += 1
 else: 
    print('Você errou a letra')
    letras_erradas += letra
    erros += 1


    def desenha_forca(erros):
     print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if ganhou:
   
   print(f'Parabéns, você acertou! A palavra era: {palavra}')
   
else:
   print(f'Você perdeu! A palavra era: {palavra}')