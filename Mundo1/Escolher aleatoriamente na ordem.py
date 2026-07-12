import random

print('Um professor decidiu sortear os alunos para apresentarem na ordem, primeiro ele precisa saber seus nomes e trabalhos')
a=input('Digite o nome do primeiro aluno e o seu trabalho: ')
b=input('Digite o nome do segundo aluno e o seu trabalho: ')
c=input('Digite o nome do terceiro aluno e o seu trabalho: ')
d=input('Digite o nome do quarto aluno e o seu trabalho: ')
lista=[a,b,c,d]
num=random.shuffle(lista)
print('A ordem de apresentação e essa:')
print('1:', lista[0])
print('2:', lista[1])
print('3:', lista[2])
print('4:', lista[3])
