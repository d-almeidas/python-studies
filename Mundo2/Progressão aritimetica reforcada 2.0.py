pt=int(input('Digite o primeiro termo da PA: '))
razao=int(input('Digite a razao da PA: '))
c=1
termo=pt

print('Os termos dessa PA são iguais a:')
while c<=10:
    print(f'{termo} -> ', end=' ')
    termo+=razao
    c+=1

q = int(input('Deseja mostrar mais quantos termos [Encerrar = 0]: '))

while q!=0:
    for c in range(q):
        print(termo, end=' - ')
        termo+=razao
        
    q = int(input('Deseja mostrar mais quantos termos [Encerrar = 0]: '))

if q==0:
    print('Encerrando')




