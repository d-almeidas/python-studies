lista = list()
maior=0
menor=0

for cont in range (1,6):
    val=int(input(f'Digite o {cont}º valor: '))
    lista.append(val)

    if cont == 1:
        maior = val
        menor = val
    else:
        if val> maior:
            maior = val
        if val < menor:
            menor = val

posicao = lista.index(maior)
posicaomenor=lista.index(menor)

print(f'Os numeros digitados foram {lista}')

print(f'O maior valor e: {maior} que esta na posição {posicao+1}....')
print(f'O menor valor e: {menor} que esta na posição {posicaomenor+1}....')




