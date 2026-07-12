def leiaint(msg):
    n=input(msg)
    if n.isnumeric():
        return int(n)
    if n == '':
        print('Usuario preferiu não digitar esse numero!')
        zero=0
        return zero

    else:
        print('Digite um numero inteiro valido!')
        return leiaint(msg)


def leiaflotat(msg):
    valido=False
    r=input(msg).replace(',','.').strip()
    if r.isnumeric():
        print(f'ERROR: "{r}" e um preço invalido!')
        return leiaflotat(msg)
    if r == '':
        print('Usuario preferiu não digitar esse numero!')
        zero=0
        return zero

    else:
        valido=True
        return float(r)


n=leiaint('Digite um numero inteiro: ')
r=leiaflotat('Digite um numero real: ')

print(f'O numero inteiro digitado foi {n} e o real foi {r}')