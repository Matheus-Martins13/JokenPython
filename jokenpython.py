"""
JokenPython - Pedra, papel e tesoura - V2
Autor: Matheus Martins

V1.0 18/07/2021
V1.2 10/02/2022

# Legenda:
- pedra: 1
- papel: 2
- tesoura: 3

"""
from random import randint
opcao_jogo = 2


def jogar():
    return randint(1, 3)


# Inicio do jogo

while opcao_jogo == 2:
    print('Seja bem vindo ao JokenPython!\n')

    user = int(input('Escolha:\n 1 - Para PEDRA; \n 2 - Para PAPEL; \n 3 - Para TESOURA \n >> '))
    comp = jogar()

    # Verificar se a opção do usuário é válida
    if user not in range(1, 4):
        print('Valor do usuário inválido.')
        break

    # --------------- Fim da Verificalção --------------

    # No caso de 'pedra'
    if user == 1 and comp == 1:
        print('Empate! Ambos escolheram pedra.')

    elif user == 1 and comp == 2:
        print('Você infelizmente perdeu. O computador jogou papel.')

    elif user == 1 and comp == 3:
        print('Parabéns, você venceu! O computador escolheu a tesoura!')

    # -----------------------------

    # No caso de 'papel'
    elif user == 2 and comp == 2:
        print('Empate! Ambos escolheram papel!')

    elif user == 2 and comp == 3:
        print('Você infelizmente perdeu. O computador jogou tesoura.')

    elif user == 2 and comp == 1:
        print('Parabéns, você venceu! O computador escolheu pedra!')

    # -----------------------------

    # No caso de 'tesoura'
    elif user == 3 and comp == 3:
        print('Empate! Ambos escolheram tesoura!')

    elif user == 3 and comp == 1:
        print('Você infelizmente perdeu. O computador jogou pedra.')

    elif user == 3 and comp == 2:
        print('Parabéns, você venceu! O computador jogou papel.')

    else:
        print('Algo deu errado, pedimos desculpas.')

    opcao_jogo = int(input('\nDigite 2 para jogar novamente ou qualquer tecla para sair. \n >> '))
    if opcao_jogo != 2:
        print('Obrigado por jogar JokenPython, volte sempre!')
