lista=[]
listai=[]
listap=[]
while True:
    n=(int(input('Digite um valor: ')))
    lista.append(n)
    q=str(input('Quer continuar? [S/N] ')).upper()
    while q not in 'SN':
        q = str(input('Quer continuar? [S/N] ')).upper()
    if q=='S':
        if n%2!=0:
            listai.append(n)

        if n%2==0:
            listap.append(n)
    if q=='N':
        if n%2!=0:
            listai.append(n)
        if n%2==0:
            listap.append(n)
        print(f'Sua lista ficou com os valores {lista}')
        if not listap:
            print('Não houve numero par')
        else:
            print(f'Sua lista com os numeros pares ficou {listap}')
        if not listai:
            print('Não houve numeros impares')
        else:
            print(f'Sua lista com os numeros impares ficou {listai}')
        break

