pop1, pop2, tx1, tx2 = map(float, input().split())
if tx2 > tx1:
    print('A nunca alcancara B.')
else:
    years = 0
    while pop1 < pop2:
        pop1 = int(pop1*(1 + tx1/100))
        pop2 = int(pop2*(1 + tx2/100))
        years += 1
    if years > 1000:
        print('Mais de um milenio.')
    else:
        print(f'Vai alcancar em {years} ano(s).')