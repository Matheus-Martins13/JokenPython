"""
JokenPython - Pedra, papel e tesoura - V2
Autor: Matheus Martins

V1.0 18/07/2021
V2 10/02/2022

# Legenda:
- pedra: 1
- papel: 2
- tesoura: 3

"""
from modules.joga import jogar
from modules.valida import valida
from time import sleep


def play_game():

    print(100 * '\n')
    print('Seja bem vindo ao JokenPython!\n')
    user = int(input('Escolha:\n 1 - Para PEDRA; \n 2 - Para PAPEL; \n 3 - Para TESOURA \n >> '))    
    comp = jogar()

    # Verificar se a opção do usuário é válida
    if user not in range(1, 4):
        print('Valor não listado!')
        sleep(2)
        play_game()
    
    resultado = valida(user, comp)
    print(resultado)

    if play_again():
        play_game()
    else:
        print('Obriado por jogar JokenPython!')
        sleep(2)
        return


def play_again():
    play = int(input('Digite 2 para jogar novamente ou qualquer tecla para sair: '))
    if play == 2:
        return True 
    return False

if __name__ == '__main__':
    play_game()
