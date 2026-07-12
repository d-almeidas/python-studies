km=int(input('Qual a distançia em KM da sua viagem: '))
preço=km*0.50
preço2=km*0.45
if km<=200:print(f'Sua viagem custara {preço}$')
elif km>200:print(f'Sua viagem vai custar {preço2}$')
