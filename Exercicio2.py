def soma_harmonica(x):
    resposta=1
    if x>1:
        resposta = ((1/x)+soma_harmonica(x-1))
    return(resposta)
