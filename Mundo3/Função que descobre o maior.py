from random import randint
lista=[]
def maior(*num):
    maiornum = num[0]
    for n in num:
        if n>maiornum:
            maiornum = n
    return maiornum
def linha():
    print('-'*30)
linha()
for i in range(0,6):
    lista.append(randint(0,10))
print(f'{lista} foram informados {len(lista)} valores ao todo')
print(f'De todos os valores {maior(*lista)} e o maior')
lista.clear()
linha()
for l in range(0,3):
    lista.append(randint(0, 10))
print(f'{lista} foram informados {len(lista)} valores ao todo')
print(f'De todos os valores {maior(*lista)} e o maior')
lista.clear()
linha()
lista.append(randint(0,10))
print(f'{lista} foram informados {len(lista)} valores ao todo')
print(f'De todos os valores {maior(*lista)} e o maior')
lista.clear()
linha()

