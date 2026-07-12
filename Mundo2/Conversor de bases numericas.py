try:
    num=int(input('Digite um numero inteiro: '))
except:
    print('Isso não e um numero inteiro viu')
    exit()
print('[1]: Para binario')
print('[2]: Para octal')
print('[3]: Para hexadecimal')
qual=int(input('Para qual conversão sera? '))

binario=bin(num)
octal=oct(num)
hexadec=hex(num)
if qual==1:
    print(f'O numero {num} em binario ficara: {binario[2:]} ')
elif qual==2:
    print(f'O seu numero {num} em octal ficara: {octal[2:]} ')
elif qual==3:
    print(f'O seu numero {num} em hexadecimal ficara: {hexadec[2:]}')
else:
    print('Base de conversão invalida')
