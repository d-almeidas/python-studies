nome=input('Digite seu nome completo: ').lower()
lista=nome.split()
primeiro=lista[0]
ultimo=lista[-1]
print(f'O seu nome: {nome}')
print(f'e presente por seu primeiro nome: {primeiro}')
print(f'e por seu ultimo nome: {ultimo}')