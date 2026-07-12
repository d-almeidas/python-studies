lsita=list()
c=0
while True:
    n = int(input('Digite um numero: '))
    q=str(input('Quer continuar? [S/N] ')).upper()
    while q not in 'SN':
        q = str(input('Quer continuar? [S/N] ')).upper()
    lsita.sort(reverse=True)

    if q=='S':
        c+=1
        lsita.append(n)
        lsita.sort(reverse=True)
    else:
        if q=='N':
            c += 1
            lsita.append(n)
            lsita.sort(reverse=True)
            print('finalizando...')
            break
print('-='*40)
print(f'Foram digitados {c} numeros ao todo')
print(f'A lista desses numeros em formato decrescente e igual a {lsita}')
if 5 in lsita:
    print(f'Possui sim o valor {5} na lista')
else:
    print(f'O valor {5} não esta na lista')
print('-='*40)


