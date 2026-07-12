from datetime import date

def voto(idade):
    if idade>=18 and idade<65:
        print('Voto obrigatorio')
    if idade>=65:
        print('Voto opcional')
    if idade<18:
        print('Voto negado')


ano=date.today().year
nascimento=int(input('Digite o ano de nascimento: '))
idade=ano-nascimento
print(f'Com {idade} anos:',end=' ')
voto(idade)