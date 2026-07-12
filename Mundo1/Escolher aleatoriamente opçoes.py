import random
a=(input('Digite o nome do primeiro aluno: '))
b=(input('Digite o nome do segundo aluno: '))
c=input('Digite o nome do terceiro aluno: ')
d=input('Digite o nome do quarto aluno: ')

l=[a,b,c,d]
num=random.choice(l)
print('O aluno escolhido foi', num)

