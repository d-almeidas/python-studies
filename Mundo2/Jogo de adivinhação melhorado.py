import random
cn=random.randint(0,10)
p=0

n=int(input('Qual numero você acha que eu pensei: '))
while n>10 or n<0:
    n = int(input('Digite um numero valido: '))
while n != cn:
    p+=1
    n = int(input('Errou, Qual numero eu pensei: '))

    if n>10:
        n = int(input('Digite um numero valido: '))

    elif n==cn:
        print(f'Parabens, você acertou com {p} tentativas')



