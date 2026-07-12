nota=float(input('Digite a primeira nota: '))
nota2=float(input('Digite a segunda nota: '))

media=(nota+nota2)/2

if media <5:
    print('\033[31mREPROVADO\033[31m')
elif media >=5 and media <=6.9:
    print('\033[33mRECUPERAÇÃO\033[33m ')
elif media >=7:
    print('\033[32mAPROVADO\033[32m')
