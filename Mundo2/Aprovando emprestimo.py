salario=float(input('Digite seu salario: '))
casa=float(input('Digite o valor do imovel: '))
emprestimo=int(input('Em quantos anos deseja pagar o imovel: '))
mensal= casa/(emprestimo*12)
excedido=0.3*salario

if mensal>excedido:
    print(f'Você não e capaz de financiar este imovel, a prestação sera de {mensal:.2f} reais')
elif mensal<excedido:
    print('Parabens, você esta apto para financiar este imovel')
