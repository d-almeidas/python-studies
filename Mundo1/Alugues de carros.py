d=int(input('Quantos dias alugado?: '))
k=float(input('Quantos Km rodados?: '))
sd=d*60
sk=k*0.15
print(f'Seu carro percorreu {d} dias, equivalendo a {sd} reais a pagar')
print(f'Voce rodou {k} kilometros, equivalendo a {sk} reais a pagar')
print(f'Sendo o total a ser pago {sd+sk} reais!')