N, P = map(int, input().split())
array = list()
for money in range(N):
    array.append(int(input()))
media = sum(array)//len(array)
print(f'media: {media}')
print(f'o rock reinara mais uma vez' if media >= P else 'rockeiros trabalhando ja')