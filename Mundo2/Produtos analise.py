g=0
pm=0
c=0
while True:
    n=(input('Digite o nome do produto: '))
    p=float(input('Preço R$: '))
    g+=p
    c += 1

    if p>=1000:
        pm+=1
    if c==1:
        menorp=p
        menor=n
    else:
        if p < menorp:
            menorp  =p
            menor=n

    q=str(input('Quer continuar? [S/N]: ')).upper()
    while q not in ('S','N'):
        print('INVALIDO!')
        q = str(input('Quer continuar? [S/N]: ')).upper()

    if q=='N':
        print('-'*40)
        print('PROGRAMA FINALIZADO!'.center(40))
        print('-'*40)
        print(f'{g} foi o gasto total')
        print(f'Possuem {pm} acima de R$1000')
        print(f'O produto mais barato se chama: \033[33m{menor}\033[m que custa \033[31m{menorp:.2f}')
        break


