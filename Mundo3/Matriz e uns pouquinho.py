
matriz=[[0,0,0],[0,0,0],[0,0,0]]
somarpar=0
soma=0
maior=0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c]=int(input(f'Digite um valor [{l},{c}]: '))

        if matriz[l][c]%2==0:
            somarpar+=matriz[l][c]

for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]',end='')
    print()

print(f'A soma dos valores pares foram {somarpar}')

for l in range(3):
    soma+=matriz[l][2]
print(f'A Soma dos valores da terceira coluna são {soma}')
print(f'O maior valor da segunda coluna e {max(matriz[1])}')

