brasileirao=('Palmeira','Flamengo','Fluminense','Atletico-PR','Bragantino','Bahia','Coritiba','São paulo','Atelitoc-MG',
             'Corinthias','Cruziero,','Botafogo','EC Vitoria','Internacional','Santos','Grêmio','Vasco da gama','Remo','Mirassol','Chapecoense')
orde=sorted(brasileirao)
chapeco=brasileirao.index('Chapecoense')

print('-'*40)
print(f'Lista de time do Brasileirao = {orde}')
print('-'*40)

print('\033[33m Os primeiros colocados \033[m'.center(40))
print('='*40)
for primeiro in brasileirao[0:5]:
    print(f'{primeiro}')
print('='*40)

print('\033[31m Os ultimos colocados \033[m'.center(40))
print('='*40)
for ultimo in brasileirao[16:]:
    print(ultimo)
print('='*40)

print(f'A chapecoense se encontra na posição {chapeco+1}')

