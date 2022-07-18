N = input()
print(int(N[::-1]) if int(N) >= 0 else int('-' + N[1:][::-1]))