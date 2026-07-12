lista=[]
dicionario={}
soma=0
f=0
listamulher=[]
lista18=[]
while True:
    dicionario['nome']=str(input('Nome: '))
    dicionario['sexo']=str(input('Sexo [M/F]: ')).upper()
    dicionario['idade']=int(input('Idade: '))
    lista.append(dicionario.copy())
    q=str(input('Quer continuar? [S/N]: ')).upper()
    while q not in 'SN':
        q = str(input('Quer continuar? [S/N]: ')).upper()

    if q in 'Nn':
        break

for c in lista:
    soma+=c['idade']
for c in lista:
    if c['sexo']=='F':
        f+=1
        listamulher.append(c['nome'])
media = soma/len(lista)
print('-'*40)
print(f'Foram cadastradas {len(lista)} pessoas')
print(f'Media das idades: {soma/len(lista)} anos')
print(f'Mulheres cadastradas: {", ".join(listamulher)}')

print('----Lista de pessoas acima da media de idade----')
for c in lista:
    if c['idade']>media:
        print(f'nome: {c["nome"]}, sexo: {c["sexo"]}, idade: {c["idade"]}')
print('<<ENCERRADO>>')
print('-'*40)