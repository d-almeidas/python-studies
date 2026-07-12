qm = 'M'
qf = 'F'

s = input('Digite seu sexo[M/F]: ').upper().strip()[0]

while s not in 'MmFf':
    print('Valor inválido. Digite novamente: ')
    s = input('Digite seu sexo[M/F]: ').upper().strip()[0]
    if s in 'MmFf':
        print(f'Sexo {s} Validado')


