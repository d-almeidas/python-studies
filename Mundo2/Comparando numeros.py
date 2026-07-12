num=int(input('Digite um numero: '))
num2=int(input('Digite outro numero: '))
if num>num2:
    print(f'O primeiro valor: {num} e maior')
elif num2>num:
    print(f'O segundo valor: {num2} e maior')
else:
    print('Não existe valor maior, os dois são iguais')