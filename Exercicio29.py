N = int(input())
problemas = 0
for n in range(N):
    if sum(map(int, input().split())) >= 2:
        problemas += 1
print(problemas)