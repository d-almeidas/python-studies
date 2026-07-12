from time import sleep

n1= float(input('Digite o primeiro valor: '))
n2= float(input('Digite o segundo valor: '))

print(f'\033[34m [1] Somar')
print(f'\033[32m [2] Multiplicar')
print(f'\033[37m [3] Maior numero')
print(f'\033[33m [4] Novos numeros')
print(f'\033[31m [5] Sair\033[m')

print('='.center(80,'='))
q=int(input('Qual opção desejada: '))
print('='.center(80, '='))

while q!=5:
    print(f'\033[34m [1] Somar')
    print(f'\033[32m [2] Multiplicar')
    print(f'\033[37m [3] Maior numero')
    print(f'\033[33m [4] Novos numeros')
    print(f'\033[31m [5] Sair\033[m')

    if q==1:
        soma = n1 + n2
        print(f'A soma dos valores e igual a {soma}')
        q = int(input('Deseja mais alguma coisa: '))
    elif q==2:
            mult= n1*n2
            print(f'A multiplicação dos valores e igual a {mult}')
            q = int(input('Deseja mais alguma coisa: '))
    elif q==3:
        maior=max(n1,n2)
        print(f'O Maior valor e igual a {maior}')
        q = int(input('Deseja mais alguma coisa: '))

    elif q==4:
            print('Digite os novos numeros')
            n1 = float(input('Digite o primeiro valor: '))
            n2 = float(input('Digite o segundo valor: '))

            print(f'[1] Somar')
            print(f'[2] Multiplicar')
            print(f'[3] Maior numero')
            print(f'[4] Novos numeros')
            print(f'[5] Sair')
            q=int(input('Qual opção desejada: '))
    elif q>5:
        print('\033[31m !!!!Este numero não esta nas opções!!!!\033[m')
        q = int(input('Deseja mais alguma coisa: '))

if q==5:
    print('\033[31m Finalizando...')
sleep(1)
print('Volte sempre!')










