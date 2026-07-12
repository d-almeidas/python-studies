from random import randint
tupla = (randint(0,100),randint(0,100),randint(0,100),randint(0,100),randint(0,100))
print(f'Os numeros gerados foram: {tupla}')

maior=tupla[0]
menor=tupla[0]

for i in range(1,len(tupla)):
    if tupla[i]>maior:
        maior=tupla[i]
    if tupla[i]<menor:
        menor=tupla[i]

print(f'Maior valor: {maior}')
print(f'Menor valor: {menor}')
