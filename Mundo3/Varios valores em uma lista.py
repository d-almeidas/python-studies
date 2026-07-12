lista=list()

while True:
    n=(float(input('Digite um valor: ')))
    if n not in lista:
        lista.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado na lista, não irei adicionar...')

    q=str(input('Quer continuar? [S/N] ')).upper()

    while q not in 'SN':
        q = str(input('Quer continuar? [S/N] ')).upper()

    if q=='N':
        print(f'Os numeros digitados foram {lista}')
        break



