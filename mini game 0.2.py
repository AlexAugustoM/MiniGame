#Coding: utf-8
#Um de meus primeiros scripts
#Autor: Alex Augusto Martinello

def linha():
    print('-' * 80)


a = 0
linha()
print("Você tem 5 chances de acertar um número aleatório de 0 à 20!")
linha()
print("Digite um número: ")
linha()
r1 = str(input(">_ "))
linha()
from random import randint
ne1 = str(randint(0, 21))


while(r1 != ne1):
        print("Que pena, você errou!!")
        linha()
        print("Tente novamente: ")
        linha()
        r1 = str(input(">_ "))
        linha()
        a = a + 1
        if a == 5:
            print("Fim de jogo!!")
            linha()
            print("Você não conseguiu completar o desafio!!")
            linha()
            break
if(r1 == ne1):
    print("Parabéns, você acertou!!")
    linha()
    print("Você precisou de ", a, " tentativas para conseguir acertar!")
    linha()
