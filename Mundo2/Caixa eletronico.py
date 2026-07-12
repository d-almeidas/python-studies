print('='*40)
print('BEM VINDO!'.center(40))
print('='*40)

v=int(input('Qual o valor do saque: '))
cedulas=[50,20,10,1]
while True:
    for c in cedulas:
        notas= v//c
        v = v%c
        if notas>0:
            print(f'{notas} nota(s) de R$ {c}')
    break


