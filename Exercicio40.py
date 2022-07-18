from math import sqrt
number, prime = int(input()), True
for n in range(2, int(sqrt(number)) + 1):
    if not number % n:
        prime = False
        break
print('Emidio' if prime and number != 1 else 'Faina')