N = int(input())
result = 0
for vector in range(N):
    result += sum(map(int, input().split()))
print('NO' if result else 'YES')