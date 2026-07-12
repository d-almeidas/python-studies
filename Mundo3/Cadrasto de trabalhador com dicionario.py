from datetime import date
ano=date.today().year

trabalho={}
trabalho['nome']=str(input('Nome: '))
nascimento=int(input('Ano de nascimento: '))
idade=ano-nascimento
trabalho['idade']=idade

trabalho['ctps']=int(input('Carteira de trabalho( 0 para: não possui ): '))

if trabalho['ctps'] != 0:
    trabalho['contrato']=int(input('Ano de contratação: '))
    trabalho['salario']=float(input('Salario: '))
    tempo=ano-trabalho['contrato']
    trabalho['aposentadoria']= idade + (35 - tempo)
    if trabalho['contrato'] != 0:
        print(f'Carteira de trabalho......: {trabalho["ctps"]}')
        print(f'Ano de contratação......: {trabalho["contrato"]}')
        print(f'Salario......: {trabalho["salario"]}')
        print(f'Aposentadoria......: {trabalho["aposentadoria"]}')


