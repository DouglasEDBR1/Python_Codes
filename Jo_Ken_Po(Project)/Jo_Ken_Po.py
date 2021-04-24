#JO-KEN-PO
from random import randint
from time import sleep

def linha (tam=20):
    return '=-' * 20

def inicio (txt):
    print(linha())
    print (txt.center(40))
    print(linha())


itens = ('PEDRA', 'PAPEL', 'TESOURA')

resposta = 'N'
while resposta == 'N':
    inicio('Vamos começar a jogar Jo Ken Po!')
    player1 = input('Pra começar, digite seu nome: ').upper()
    resposta = input('Deseja continuar? S/N: ').upper()
    if resposta == 'S':
        print(linha())
        print(f'Seja bem vindo(a) {player1}!')
        print(linha())

resposta = 'S'
while resposta == 'S':
    computador = randint (0, 2)
    inicio ('Jo Ken Po!')

    print('''Escolha sua jogada:
    [ 0 ] PEDRA
    [ 1 ] PAPEL
    [ 2 ] TESOURA''')
    print(linha())
    player = int(input('Qual a sua jogada? '))

    print('PEDRA')
    sleep(1)
    print('PAPEL')
    sleep(1)
    print('TESOURA!')
    sleep(1)
    print(linha())
    print(f'COMPUTADOR jogou {itens[computador]}')
    print(f'{player1} jogou {itens[player]}')
    print(linha())
    if computador == 0:
        if player == 0:
            print('RESULTADO: EMPATE!')
            print(linha())
            resposta = input('Deseja continuar? S/N ').upper()
        elif player == 1:
            print(f'RESULTADO: JOGADOR {player1} VENCE!')
            print(linha())
            resposta = input('Deseja continuar? S/N ').upper()
        elif player == 2:
            print ('RESULTADO: COMPUTADOR VENCE!')
            print(linha())
            resposta = input('Deseja continuar? S/N ').upper()
        else:
            print('JOGADA INVÁLIDA!')
            print(linha())
            resposta = input('Deseja continuar? S/N ').upper()

    elif computador == 1:
        if player == 0:
            print ('RESULTADO: COMPUTADOR VENCE!')
            print(linha())
            resposta = input('Deseja continuar? S/N ').upper()
        elif player == 1:
            print ('RESULTADO: EMTATE!')
            print(linha())
            resposta = input('Deseja continuar? S/N ').upper()
        elif player == 2:
            print (f'RESULTADO: {player1} VENCE!')
            print(linha())
            resposta = input('Deseja continuar? S/N ').upper()
        else:
            print('Jogada Inválida!')
            print(linha())
            resposta = input('Deseja continuar? S/N ').upper()

    elif computador == 2:
        if player == 0:
            print(f'RESULTADO: {player1} VENCE!')
            print(linha())
            resposta = input('Deseja continuar? S/N ').upper()
        elif player == 1:
            print ('RESULTADO: COMPUTADOR VENCE!')
            print(linha())
            resposta = input('Deseja continuar? S/N ').upper()
        elif player == 2:
            print ('RESULTADO: EMPATE!')
            print(linha())
            resposta = input('Deseja continuar? S/N ').upper()
        else:
            print('JOGADA INVÁLIDA!')
            print(linha())
            resposta = input('Deseja continuar? S/N ').upper()