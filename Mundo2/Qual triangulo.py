t1=float(input('Digite a primeira reta: '))
t2=float(input('Digite a segunda reta: '))
t3=float(input('Digite a terceira reta: '))

#Condição
if t1 + t2 > t3 and t1 + t3 > t2 and t2 + t3 > t1:
    print('E um triangulo ')

    if t1==t2==t3:
        print('E um triangulo equilatero')

    elif t1==t2 or t1==t3 or t2==t3:
        print('E um triangulo isoceles')

    else:
        print('E um triangulo escaleno')

else:
    print('Não e um triangulo')


