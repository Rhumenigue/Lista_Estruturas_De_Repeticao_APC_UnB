lista = []

while True:
    nota=int(input())
    if nota != -1:
        lista.append(nota)
    else:
        media = (sum(lista)/len(lista))
        print(f'{int(media)}')
        break
        