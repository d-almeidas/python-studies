lista=[]
e=input('Digite a expressão: ')
for simbolo in e:
    if simbolo == '(':
        lista.append(simbolo)

    if simbolo == ')':
        if len(lista)>0:
            lista.pop()
        else:
            print('Lista invalida')
            break

if len(lista)==0:
    print('Lista valida')
else:
    print('Lista invalida')



