import re
N = int(input())
for i in range(N):
    string = input()
    letters = filter(lambda x: x != '', re.split(r'[0-9]', string))
    numbers = filter(lambda x: x != '', re.split(r'[A-z]', string))
    print(''.join([letter*int(number) for letter, number, in zip(letters, numbers)]))