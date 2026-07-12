from datetime import date
maiores=0
menores=0

for c in range(7):
    ano=int(input('Digite o ano de nascimento: '))

    atual=date.today().year
    idade= atual- ano

    if idade<18:
        menores += 1
    elif idade>=18:
        maiores += 1

print(f'{menores} pessoas menores de idade')
print(f'{maiores} pessoas maiores de idade')

