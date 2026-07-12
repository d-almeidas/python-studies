dado=list()
lista=list()
c=0
cn=0
while True:
    c += 1
    nome=str(input('digite seu nome: '))
    lista.append(nome)
    peso=float(input('digite seu peso: '))
    lista.append(peso)
    dado.append(lista[:])
    lista.clear()

    q=str(input('Quer continuar?[S/N]: ')).upper()
    while q not in 'SN':
        q = str(input('Quer continuar?[S/N]: ')).upper()

    while q!='N':
        c += 1
        nome = str(input('digite seu nome: '))
        lista.append(nome)
        peso = float(input('digite seu peso: '))
        lista.append(peso)
        dado.append(lista[:])
        lista.clear()
        q = str(input('Quer continuar?[S/N]: ')).upper()

        if q=='N':
            break

    maior = max(p[1] for p in dado)
    menor = min(p[1] for p in dado)

    nomemaior = []
    nomemenor = []

    for p in dado:
        if p[1] == maior:
            nomemaior.append(p[0])

        if p[1] == menor:
            nomemenor.append(p[0])

        cn+=1
    print(f'foram cadrastadas {c} pessoas')
    print(f'Maior peso e o de {nomemaior} com {maior} Kg')
    print(f'Menor peso e o de {nomemenor} com {menor} Kg')
    break

