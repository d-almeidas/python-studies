import json

from pathlib import Path

CAMINHO = Path(__file__).parent / 'dados' / 'pessoas.json'

with open(CAMINHO, 'r', encoding='utf-8') as arquivo:
    acumuladordepessoas = json.load(arquivo)

def salvar_pessoas():
    with open(CAMINHO, 'w', encoding='utf-8') as arquivo:
        json.dump(acumuladordepessoas, arquivo, indent=4)

def apagar_pessoa():
    if not acumuladordepessoas:
        print('Nenhuma pessoa cadastrada.')
        return

    print('=' * 40)
    print('PESSOAS CADASTRADAS'.center(40))
    print('=' * 40)

    for i, pessoa in enumerate(acumuladordepessoas, start=1):
        print(f'{i} - {pessoa["nome"]} ({pessoa["idade"]} anos)')

    try:
        opcao = int(input('Número da pessoa que deseja apagar: '))

        if 1 <= opcao <= len(acumuladordepessoas):
            confirmacao = input('Tem certeza? [S/N] ').strip().upper()
            if confirmacao == 'S':
                removida = acumuladordepessoas.pop(opcao - 1)
                salvar_pessoas()
                print(f'{removida["nome"]} foi removido(a) com sucesso!')
            else:
                print('Pessoa não encontrada.')
    except ValueError:
        print('Digite um número válido.')
        
def cadastro(nome, idade):
    pessoas ={}
    print(f'Cadastro concluido: {nome} - {idade}')
    pessoas['nome'] = nome
    pessoas['idade'] = idade
    acumuladordepessoas.append(pessoas)
    salvar_pessoas()

def cadastrotitulo():
    print('=' * 40)
    print('NOVO CADASTRO'.center(40))
    print('=' * 40)

def pessoastiutlo():
    print('=' * 40)
    print('PESSOAS CADASTRADAS'.center(40))
    print('=' * 40)

def pessoas_cadastradas():
    for j in acumuladordepessoas:
        print(f'{j["nome"]}        \t{j["idade"]}')

