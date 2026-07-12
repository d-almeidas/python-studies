n=int(input('Digite um numero: '))
n1=int(input('Digite um numero: '))
n2=int(input('Digite um numero: '))
n3=int(input('Digite um numero: '))
par=0
tupla=n,n1,n2,n3

print(f'Você digitou os numeros {tupla}')

print(f'O numero 9 apareceu: {tupla.count(9)} vezes')

if 3 not in tupla:
    print('Não teve o numero 3')
else:
    print(f'O numero 3 apareceu a primeira vez na posição {tupla.index(3) + 1}')

for c in tupla:
    if c %2==0:
        par=par+1
print(f'Quantidade de numeros pares: {par}')



