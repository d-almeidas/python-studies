pt=int(input("digite o primeiro termo: "))
razao=int(input("digite a razao: "))
decimo= pt+(10-1) * razao

print('A progressão dessa PA: ')
for c in range(pt, decimo+razao, razao):
    pt += razao

    print(pt, end=' ')
print('ACABOU')