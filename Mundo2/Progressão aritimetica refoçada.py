pt=int(input('Digite o primeiro termo da PA: '))
razão=int(input('Digtie a razão da PA: '))

c=1
termo=pt

while c <= 10:
    print(f'{termo} -> ', end=' ')
    termo+= razão
    c+=1

