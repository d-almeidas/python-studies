idade=0
maisvelho=0
nome=0
menordeidd=0
nomemaisvelho=0
si=0

for c in range(1,5):
    print(f'Pessoa {c}')
    nome=str(input('Digite seu nome: ')).upper().strip()
    try:
        idade=int(input('Digite sua idade: '))
    except:
        print('ERROR, tente novamente')
        idade = int(input('Digite sua idade: '))

    sexo=str(input('Digite seu sexo [M/F]: ')).upper().strip()


    while sexo not in 'MF':
        print('Opção invalida')
        sexo=str(input('Digite seu sexo: ')).upper().strip()

    si += idade
    media = si/4

    if sexo=='M'==1 :
        maisvelho=idade
        maisvelho=nome

    elif sexo=='F' and idade<20==1:
        menoridd= menordeidd+1

    else:
        if sexo=='M' and idade>maisvelho:
            maisvelho=idade
            nomemaisvelho=nome

        elif sexo=='F' and idade < 20:
            menordeidd= menordeidd+1

print(f'A media de idade do grupo e igual a {media}')
if maisvelho==0:
    print('Não possui nenhum homem')
else:
    print(f'O Homem com maior idade e o {nomemaisvelho} que tem {maisvelho} anos')
print(f'Possue {menordeidd} Mulhere(s) menores de 20 anos')










