def valida(user, comp):
    # No caso de 'pedra'
    if user == 1 and comp == 1:
        return 'Empate! Ambos escolheram pedra.'
    if user == 1 and comp == 2:
        return 'Você infelizmente perdeu. O computador jogou papel.'
    if user == 1 and comp == 3:
        return'Parabéns, você venceu! O computador escolheu tesoura!'
    # No caso de 'papel'
    if user == 2 and comp == 2:
        return 'Empate! Ambos escolheram papel!'
    if user == 2 and comp == 3:
        return 'Você infelizmente perdeu. O computador jogou tesoura.'
    if user == 2 and comp == 1:
        return 'Parabéns, você venceu! O computador escolheu pedra!'
    # No caso de 'tesoura'
    if user == 3 and comp == 3:
        return 'Empate! Ambos escolheram tesoura!'
    if user == 3 and comp == 1:
        return 'Você infelizmente perdeu. O computador jogou pedra.'
    if user == 3 and comp == 2:
        return 'Parabéns, você venceu! O computador jogou papel.'
    # Default
    return 'Algo deu errado, pedimos desculpas.'
