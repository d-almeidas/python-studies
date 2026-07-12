from time import sleep
c=0
def linha():
    print('-'*30)

def contagem(a,b,c):
    if c == 0:
        c = 1

    if c<0:
        c=-c

    if a<b:
        while a<=b:
            print(a,end=' ')
            sleep(0.5)
            a+=c


    if b<a:
        while b<=a:
            print(a,end=' ')
            sleep(0.5)
            a-=c
linha()
print('contagem de 1 ate 10 de 1 em 1')
for l in range(1,11):
    c+=1
    print(l, end=' ')
print()

linha()
linha()
print('contagem de 10 ate 0 de 2 em 2')
for h in range(10,0,-2):

    print(h,end=' ')
print()

linha()
linha()
print('SUA VEZ de personalizar a contagem')
inicio=int(input('inicio: '))
final=int(input('final: '))
passo=int(input('passo: '))
contagem(inicio,final,passo)
print('FIM')
