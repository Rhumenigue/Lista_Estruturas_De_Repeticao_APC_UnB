N = int(input())
array = list(map(int, input().split()))
maximum = max(array)
for n in map(lambda x: maximum-x, array):
    print(n, end=' ')