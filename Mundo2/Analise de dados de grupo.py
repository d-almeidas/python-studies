p18=0
p=0
m=0
f=0

while True:
    print('-'*40)
    p+=1

    i=int(input('Digite a idade: '))

    if i >= 18:
        p18 += 1

    s=str(input('Masculino ou feminino[M][F]: ')).upper()
    while s not in ('M', 'F'):
        print('Invalido')
        s = str(input('Masculino ou feminino[M][F]: ')).upper()


    print('-' * 40)
    if s=='M':
        m+=1
    else:
        if s=='F' and i<20:
            f+=1

    q=str(input('Quer continuar?[S/N]: ')).upper()
    while q not in ('S', 'N'):
        print('Invalido')
        q = str(input('Quer continuar?[S/N]: ')).upper()
    nao='N'

    if q==nao:
        print('='*40)
        print('FIM DO PROGRAMA'.center(40))
        print('='*40)
        print(f'Possuem {p} pessoas ao todo')
        print(f'{p18} Maiores de 18 anos')
        print(f'{m} Homens cadastrados')
        print(f'{f} Mulher(es) menor(es) de 20 anos cadastrada(s)')
        break