qtd_alunos = int(input())

for i in range (0, qtd_alunos):
    nota1, nota2, nota3 = map(float, input().split())
    media = ((nota1+nota2+nota3)/3)
    if media >= 7.0:
        print(f'O ALUNO {i} FOI APROVADO')
    else:
        print(f'O ALUNO {i} FOI REPROVADO')