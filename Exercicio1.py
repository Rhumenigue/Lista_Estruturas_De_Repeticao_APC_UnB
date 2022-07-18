def anobissexto(a):
    if a%4 == 0 and a%100 != 0 or  a%400 == 0:
        return('Sim')
    else:
        return('Nao')
        