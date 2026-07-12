from datetime import date

ano=int(input('Digite o ano de nascimento: '))
atual=date.today().year
idade=atual-ano
falta=18-idade
passou=idade-18

if idade<18:
    print(f'Você ainda não precisa fazer o alistamento militar, faltam {falta} anos para o alistamento militar')
elif idade==18:
    print('Você ja pode se alistar, entre no aplicativo gov.com.br')
elif idade>18:
    print(f'O tempo de alistamento já passou faz {passou} ano(s), procure \033[31mIMEDIATAMENTE\033[m o alistamento militar')