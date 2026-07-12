c=0
soma=0
n=int(input('Digite um valor: '))
while n!=999:
    soma+=n
    c+=1
    n=int(input('[999Cancelar]  Digite um valor: '))
    if n==999:
        print(f' Foram digitados {c} numeros e sua soma e igual a {soma}')

