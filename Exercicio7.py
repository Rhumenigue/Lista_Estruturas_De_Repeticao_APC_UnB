dollar = float(input())
lote = int(input())
qtd = int(input())

conta = dollar*lote
percentual = 1.025

for i in range (1, qtd+1):
    print(f'Lote: {i} - Total da venda: R$ {conta*percentual:.2f}')

    