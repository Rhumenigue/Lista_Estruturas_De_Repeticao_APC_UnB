a, b = map(int, input().split())
greater, lesser = max(a, b), min(a, b)
if not greater % lesser or (greater % lesser > 1 and not (greater % (greater % lesser))):
    print('Nao sao co-primos!')
else:
    print('Sao co-primos.')