c=0
soma=0
while True:
    n = int(input('Digite o valor: '))
    if n==999:
        break
    c += 1
    soma += n
print(f'Foram digitados {c} numeros e sua somas valem {soma}')