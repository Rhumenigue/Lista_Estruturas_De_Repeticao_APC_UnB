N = int(input())
S, result = input(), ''
for index in range(N-1):
    if S[index+1] < S[index]:
        result = S[index]
        break
if result != '':
    print(S.replace(result, '', 1))
else:
    print(S[:-1])