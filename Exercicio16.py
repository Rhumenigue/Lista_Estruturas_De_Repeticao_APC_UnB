N = int(input())
king = 0
for person in range(N):
    money = int(input())
    if money < 1000:
        king += 1000-money
print(king)