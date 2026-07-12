def leiaint(msg):
    n=input(msg)
    if n.isnumeric():
        return int(n)
    else:
        print('Error, digite um numero inteiro valido')
        return leiaint(msg)
    
n= leiaint('Digite um numero: ')
print(f'o numero digitado foi {n}')


