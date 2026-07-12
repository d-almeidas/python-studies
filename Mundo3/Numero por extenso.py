numeros=('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez',
          'onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')

while True:
    n=int(input('digite um numero de 0 ate 20: '))
    while n < 0 or n > 20:
        n = int(input('Digite um numero \033[31mvalido\033[m de 0 ate 20: '))
    print(f'O numero digitado foi o numero {numeros[n]}')
    q=str(input('Quer continuar[S/N]: ')).upper()
    while q not in 'SN':
        q = str(input('Digite uma letra \033[31mvalida\033[m entre[S/N]: ')).upper()

    if q=='S':
        n = int(input('digite um numero de 0 ate 20: '))
        while n < 0 or n > 20:
            n = int(input('Digite um numero \033[31mvalido\033[m de 0 ate 20: '))
        print(f'O numero digitado foi o numero {numeros[n]}')
        q = str(input('Quer continuar[S/N]: ')).upper()
        while q not in 'SN':
            q = str(input('Digite uma letra \033[31mvalida\033[m entre[S/N]: ')).upper()
    if q=='N':
        print('finalizando...')
        break




