import re
password = input()
if re.match(r'(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])', password) and not re.match(r'(?=.*\W)', password) and 32 >= len(password) >= 6:
    print('Senha valida.')
else:
    print('Senha invalida.')