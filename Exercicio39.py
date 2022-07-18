string = '.' + input() + '.'
print(sum(map(lambda x, y: 1 if x == 'o' and y != x else 0, string[:-1], string[1:])))