from time import sleep
c=0
soma=0
maior=0
menor=0
r='S'

while r!='N':
    nu = float(input('Digite o valor: '))
    c += 1
    soma += nu
    r = str(input('Quer continuar? [S/N] ')).upper().strip()
    while r not in ('S', 'N'):
        print('Digite uma opcao valida')
        r = str(input('Quer continuar? [S/N] ')).upper().strip()

    if c==1:
        maior=nu
        menor=nu
    else:
        if nu>maior:
            maior=nu
        elif nu<menor:
            menor=nu

media = soma / c
if r=='N':
    print('Finalizando')
    sleep(1)
print(f'O maior numero foi {maior} e o menor {menor}')
print(f'Você digitou {c} numeros e a media entre eles e iguail a {media:.2f}')

