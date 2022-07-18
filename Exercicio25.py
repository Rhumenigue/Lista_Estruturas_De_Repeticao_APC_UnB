def ppa(p1, p2):
    if p1 == p2 == 1:
        return 'Sem ganhador'
    elif p1 == p2 == 2:
        return 'Ambos venceram'
    elif p1 == p2 == 3:
        return 'Aniquilacao mutua'
    elif (p1 == 3) or (p1 == 1 and p2 == 2):
        return 'Jogador 1 venceu'
    else:
        return 'Jogador 2 venceu'