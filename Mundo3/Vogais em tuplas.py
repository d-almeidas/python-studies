dbd='Desconhecido','Draga','Mikaella','Renato','Wesker','Blight','James'
vogais='a','e','i','o','u'


for nome in dbd:
    print('=' * 40)
    print(f'Em \033[31m{nome}\033[m temos as vogais:',)
    print('='*40)

    for letra in nome:
        if letra in vogais:
            print(f'\033[33m{letra}\033[m')



