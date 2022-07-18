contador = int(input())
lista = []

for i in range (1, contador+1):
    numero = int(input())
    lista.append(numero)
print(f'Menor: {min(lista)}')
print(f'Maior: {max(lista)}')



