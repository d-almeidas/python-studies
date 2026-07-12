import random
from time import sleep
i=0

print('='*40)
print('Vamos Jogar impar ou par'.center(40))
print('='*40)

while True:
    num = int(input('Digite um numero: '))
    impa = str(input('Impar ou par [I][P]: ')).upper()
    c = random.randint(0, 10)
    s = num + c

    if s % 2 != 0:
        sn = 'I'
    else:
        sn = 'P'
    if sn == impa:
        i += 1
        print(f'Você ganhou! Eu tinha pensado no {c}')
        print('Vamos jogar novamente...')
        sleep(1)

    else:
        print(f'Você perdeu com {i} vitorias consecutivas, eu tinha digitado {c}')
        break







