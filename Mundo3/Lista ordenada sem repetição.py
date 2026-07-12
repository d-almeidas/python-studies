lista=list()
inserir=False

for c in range(0,5):
    n=(int(input('Digite um numero: ')))

    for pos,valor in enumerate(lista):
        if n<=valor:
            lista.insert(pos,n)
            inserir=True
            break
    else:
        lista.append(n)
print(lista)
