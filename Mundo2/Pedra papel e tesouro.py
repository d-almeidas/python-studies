import random
from time import sleep

print('[1]: Pedra')
print('[2]: Papel')
print('[3]: Tesoura')
try:
    opcao=int(input('Qual a você vai escolher: '))


except:
    print('Este algoritimo não e valdio')
    exit()

ppt=random.randint(1,3)

print('Estou pensando no meu...')
sleep(2)

if opcao <1 or opcao>3:
    print('Opa!!, espera ai, este numero e invalido viu, DIGITE OUTRO dentro das normas')

elif ppt==opcao:
    print('Olha!, Empatamos')

elif ppt==1 and opcao==2:
    print('Perdi!, eu tinha escolhido Pedra')

elif ppt==1 and opcao==3:
    print('Ganhei!, eu tinha escolhido Pedra'
          )
elif ppt==2 and opcao==1:
    print('Ganhei!,eu tinha escolhido Papel')

elif ppt==2 and opcao==3:
    print('Perdi!, eu tinha escolhido Papel')

elif ppt==3 and opcao==1:
    print('Perdi!, eu tinha escolhido Tesoura')

elif ppt==3 and opcao==2:
    print('Ganhei!, eu tinha escolhido Tesoura')