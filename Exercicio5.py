lista = list(map(int, input().split()))

tamanho = len(lista)
total = 0

for i in range (tamanho-1):
    for j in range (tamanho - i - 1):
        if lista[j] > lista[j+1]:
            lista[j], lista [j+1] = lista[j+1], lista[j]
            total =  total + 1
print(total)