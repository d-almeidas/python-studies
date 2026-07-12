n1= float(input('Digite a primeira nota: '))
n2= float(input('Digite a segunda nota: '))
n3= float(input('Digite a terceira nota: '))
m= (n1+n2+n3)/3
print(f'Sua media entre {n1},{n2} e {n3} e igual a {m:.2f}', end=' ')
if m < 7:
    print('Infelizmente vc foi: Reprvado KKKKK')


else:
    print('Parabens vc foi: Aprovado')