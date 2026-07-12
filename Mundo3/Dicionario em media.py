media={}
n=str(input('digite o nome do aluno: '))
media['nome'] = n
med=float(input('Digite a media do aluno: '))
media['Media']=med

if media['Media'] >= 7:
    print(f'O aluno \033[31m{n}\033[m com media: \033[33m{med}\033[m foi aprovado')
if media['Media'] <7:
    print(f'O aluno \033[31m{n}\033[m com media: \033[33m{med}\033[m foi reprovado')