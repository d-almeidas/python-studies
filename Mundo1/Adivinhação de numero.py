import random
from time import sleep
n=random.randint(0,10)
usu=input('Tente adivinhar o numero: ')
print('Hmmmmmm.......')
sleep(2)
if usu==n:print('\033[33mParabens!!! Voce acertou\033[33m')
else:
    print('\033[31mVoce errou\033[31m')
print(f'\033[37mEste foi o numero: {n}\033[37m')
