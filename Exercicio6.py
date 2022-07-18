N = int(input())
array = list(map(int, input().split()))
minimum = min(array)
print(*map(lambda x: x-minimum, array))