#Um número primo é um número inteiro maior que 1 que é divisı́vel apenas por 1
# e por ele mesmo. Um #número a é divisível por b se o resto da divisão de
#  a por b é zero. Dessa forma implemente as funções #chamadas (1) ehPrimo, 
# que recebe um inteiro 1≤𝑥≤106 e retorna se o valor é ou não primo,
#  e (2) #divisoresPrimos que recebe um inteiro 1≤𝑥≤106 e retorna a quantidade de divisores primos.
# #Entrada 
#A função ehPrimo recebe como parâmetro um único inteiro 1≤𝑥≤106. 
# A função divisoresPrimos #recebe como parâmetro um único inteiro 1≤𝑥≤106. 
#Saída 
#A função ehPrimo retorna 1 caso 𝑥 seja primo e 0 caso contrário. 
# A função divisoresPrimos retorna #a quantidade de divisores primos do inteiro 𝑥 recebido.

def ehPrimo(x):
    total = 0
    x = int(x)
    for i in range(1, x+1):
        if x % i == 0:
            total += 1

    if total == 2:
        return(0)
    else:
        return(1)

def divisoresPrimos(number):
    result = 0
    for n in range(2, number//2 + 1):
        if not number % n and ehPrimo(n):
            result += 1
    return result

        
    
    

    