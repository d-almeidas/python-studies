from random import randint
numeros=[]

def sorteia():
    for c in range(0,5):
        numeros.append(randint(0,10))
        print(numeros[c],end=' ')

def somapar():
    somar = 0
    for l in numeros:
        if l%2==0:
            somar+=l
    print(somar)

print(f'Os numeros sorteados foram: ',end=' ')
sorteia()

print()

print(f'A soma dos numeros pares são: ',end=' ')
somapar()