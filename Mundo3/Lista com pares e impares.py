lista=list()
listapar=list()
listaimpar=list()

for c in range(1,8):
    v=int(input(f'Digite o {c} valor: '))
    lista.append(v)
    if v%2==0:
        listapar.append(v)

    else:
        listaimpar.append(v)

    listapar.sort()
    listaimpar.sort()
print(f'Os valores digitados foram {lista}')
print(f'Os valores pares em ordem crescente foram {listapar}')
print(f'Os valores impares em ordem crescente foram {listaimpar}')