from time import sleep
c=0
print('='*40)
print('Tabuada'.center(40))
print('='*40)
while True:
    n = int(input('Qual valor deseja ver a tabuada?: '))
    c+=1

    if n<0:
        print('Encerrando..')
        sleep(1)
        print('Obrgado, volte sempre!')
        break

    else:
        for i in range(1,11):
            tab=n*i
            print(f'{n} x {i} = {tab}')
