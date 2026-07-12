maior=0
menor=0

for c in range(1,6):
    p=float(input(f'{c} Peso: '))

    if c==1:
        maior=p
        menor=p
    else:
        if p>maior:
            maior=p
        elif p<menor:
            menor=p

print(f'\033[33m O MAIOR PESO E IGUAL A {maior} \033[m')
print(f'\033[33mO MENOR PESO IGUAL A {menor}\033[m')




