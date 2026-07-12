num=(int(input('Digite seu numero de 0 a 9999: ')))
unidade=num%10
centena=(num//100)%10
dezena=num//10%10
milhar=num//1000%10
print(f'Unidade: {unidade}')
print(f'Centena: {centena}')
print(f'Dezena: {dezena}')
print(f'Milhar: {milhar}')
