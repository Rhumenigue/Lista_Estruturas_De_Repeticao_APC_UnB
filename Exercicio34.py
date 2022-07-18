C = int(input())
result = -1
for index, number in enumerate(sorted(map(int, input().split()))):
    if number >= C:
        result = index
        break
print(result)