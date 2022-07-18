N = int(input())
value = 0
for i in range(N):
    x = input()
    if x == '++X' or x == 'X++':
        value += 1
    else:
        value -= 1
print(value)