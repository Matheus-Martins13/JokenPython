"""
JokenPython - Pedra, papel e tesoura
Autor: Matheus Martins
Data: 18/07/2021

# Legenda para as regras de definição:
- pedra: round(random(), 2) <= 0.33

- papel: 0.33 > round(random(), 2) <= 0.66

- tesoura: 0.66 > round(random(), 2)

"""
from random import random

opcao_jogo = 2

# Inicio do jogo

while opcao_jogo == 2:
    print('Seja bem vindo ao JokenPython!\n')

    user = int(input('Escolha:\n 1 - Para PEDRA; \n 2 - Para PAPEL; \n 3 - Para TESOURA \n >>>> '))

    # Verificar se a opção do usuário é válida
    if user <= 0 or user >= 4:
        print('Valor do usuário inválido.')
        break

    # --------------- Fim da Verificalção --------------

    # No caso de 'pedra'
    if user == 1 and round(random(), 2) <= 0.33:
        print('Empate! Ambos escolheram pedra.')

    elif user == 1 and 0.33 > round(random(), 2) <= 0.66:
        print('Você infelizmente perdeu. O computador jogou papel.')

    elif user == 1 and 0.66 > round(random(), 2):
        print('Parabéns, você venceu! O computador escolheu a tesoura!')

    # -----------------------------

    # No caso de 'papel'
    elif user == 2 and 0.33 > round(random(), 2) <= 0.66:
        print('Empate! Ambos escolheram papel!')

    elif user == 2 and 0.66 > round(random(), 2):
        print('Você infelizmente perdeu. O computador jogou tesoura.')

    elif user == 2 and round(random(), 2) <= 0.33:
        print('Parabéns, você venceu! O computador escolheu pedra!')

    # -----------------------------

    # No caso de 'tesoura'
    elif user == 3 and 0.66 > round(random(), 2):
        print('Empate! Ambos escolheram tesoura!')

    elif user == 3 and round(random(), 2) <= 0.33:
        print('Você infelizmente perdeu. O computador jogou pedra.')

    elif user == 3 and 0.33 > round(random(), 2) <= 0.66:
        print('Parabéns, você venceu! O computador jogou papel.')

    else:
        print('Algo deu errado, pedimos desculpas.')

    opcao_jogo = int(input('\nDigite 2 para jogar novamente ou qualquer tecla para sair. \n >>>> '))
    if opcao_jogo != 2:
        print('Obrigado por jogar JokenPython, volte sempre!')

