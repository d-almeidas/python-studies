def tituloverde(msg):
    tam=len(msg)
    print('\033[32m'+'~'*tam)
    print(msg)
    print('~'*tam,'\033[m')


def tituloazul(msg):
    texto=f'Acessando o manual de comando {msg}'
    tam=len(texto)+4
    print('\033[34m-'+'-'*tam)
    print(texto)
    print('-' * tam + '\033[m')

#Program principal
while True:
    tituloverde('Sistema interativo de ajuda PYHELP')
    digite=str(input('Função ou biblioteca: '))
    if digite.upper() == 'FIM':
        print('\033[31m Ate logo!!')
        break
    else:
        tituloazul(digite)
        help(digite)



