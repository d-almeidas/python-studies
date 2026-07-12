print('='*40)
print('BEM VINDO!'.center(40))
print('='*40)

v=int(input('Qual o valor do saque: '))
while True:
    if v>=50:
            notasde50=  v//50
            v= v%50
            print(f'{notasde50} notas de 50')
    if v>=20:
            notasde20= v//20
            v= v%20
            print(f'{notasde20} notas de 20')
    if v>=10:
            notasde10= v//10
            v= v%10
            print(f'{notasde10} notas de 10')
    if v>=1:
            notasde1= v//1
            v= v%1
            print(f'{notasde1} notas de 1')
    print('-'*40)
    print('Tenha um bom dia!'.center(40))
    print('-'*40)
    break