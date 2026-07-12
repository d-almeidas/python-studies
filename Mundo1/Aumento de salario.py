salario=float(input('Digite o seu salario: '))

aumento=salario*1.10
aumento2=salario*1.15

if salario>=1250.00:
    print(f'Seu salario saiu de {salario} e foi para: {aumento:.2f} com o aumento de 10% no valor')
else:
    print(f'Seu salario sai de {salario} e foi para: {aumento2:.2f} com o aumento de 15% no valor')