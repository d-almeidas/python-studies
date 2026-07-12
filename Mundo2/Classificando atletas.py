from datetime import date
anoAtual = date.today().year
try:
    nasc=int(input('Digite o ano de nascimento: '))
except:
    print('Não e uma data')
    exit()
idade = anoAtual - nasc

if idade <=9:
    print('Mirim')
elif idade >9 and idade <=14:
    print('Infantil')
elif idade >14 and idade <=19:
    print('Junior')
elif idade >19 and idade <=20:
    print('Senior')
elif idade >20 :
    print('Master')
