r1=float(input('Digite a primeira reta: '))
r2=float(input('Digite a segunda reta: '))
r3=float(input('Digite a terceira reta: '))

#CONDIÇÃO
reta1= r1+r2>r3
reta2= r1+r3>r2
reta3= r2+r3>r1

if reta1 and reta2 and reta3:print('e um triangulo')
else:print('Não e um triangulo')