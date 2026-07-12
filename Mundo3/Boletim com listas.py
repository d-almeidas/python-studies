from time import sleep
listanome = []
listanota1= []
listanota2= []

while True:
    nome=str(input('Digite o nome do auluno: '))
    listanome.append(nome)
    nota1=float(input('Digite a primeira nota: '))
    listanota1.append(nota1)
    nota2=float(input('Digite a segunda nota: '))
    listanota2.append(nota2)
    q=str(input('Quer continuar? [S/N] ')).upper()


    if q == 'N':
        print('-=' * 40)
        print('No. NOME              MEDIA')
        print('-' * 40)
        for c in range(len(listanota1)):
            media = (listanota1[c] + listanota2[c]) / 2
            print(f'{c:<4}{listanome[c]:<5}            {media:.1f}')
        break
while True:
    mostrar=int(input('Qual aluno deseja mostrar a nota? (999 para sair): '))
    if mostrar == 999:
        print('Finalizando...')
        sleep(1)
        print('Volte sempre!')
        break

    if mostrar >=0 and mostrar <= len(listanome):
        print(f'Aluno: {listanome[mostrar]}')
        print(f'Nota 1: {listanota1[mostrar]}')
        print(f'Nota 2: {listanota2[mostrar]}')
    else:
        print(f'Aluno inexistente')
