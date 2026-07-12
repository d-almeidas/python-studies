preço=float(input('Digite o preço do produto: '))
print('[1]: A vista no dinheiro ou cheque ')
print('[2]: A vista no cartão ')
print('[3]: 2X no cartão ')
print('[4]: 3X ou mais no cartão ')

opcao=int(input('Qual a forma de pagamento: '))

DC=0.9*preço
C=0.95*preço
C2X=preço
C3X=1.2*preço

if opcao== 1:
    print(f'O produto ficou{DC:.2f}$')
elif opcao==2:
    print(f'O produto ficou{C:.2f}$')
elif opcao==3:
    print(f'O produto ficou{C2X:.2f}$')
elif opcao==4:
    print(f'O produto ficou{C3X:.2f}$')