K, L, M, N = int(input()), int(input()), int(input()), int(input())
D = int(input())
numbers, final = list(range(1, D+1)), 0
for dragon in sorted([K, L, M, N]):
    index = 0
    while index < len(numbers):
        if not numbers[index] % dragon:
            numbers.pop(index)
            final += 1
        else:
            index += 1
print(final)