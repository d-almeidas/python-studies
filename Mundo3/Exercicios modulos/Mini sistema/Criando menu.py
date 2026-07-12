import Cadastrocurso
def menu():
    print('=' * 40)
    print('MENU PRINCIPAL'.center(40))
    print('=' * 40)
    print('\033[33m1\033[m - \033[34mVer pessoas cadastradas\033[m')
    print('\033[33m2\033[m - \033[34mCadastrar nova Pessoa\033[m')
    print('\033[33m3\033[m - \033[34mApagar pessoa cadastrada\033[m')
    print('\033[33m4\033[m - \033[34mSair\033[m')
    print('=' * 40)
    
while True:
    menu()
    try:
        opcao = int(input('Sua opção: '))
    except ValueError:
        print('\033[31mErro! Digite uma opção válida.\033[m')
        continue
    
    if opcao == 4:
        print('\033[31mObrigado volte sempre!\033[m')
        break

    elif opcao == 1:
        Cadastrocurso.pessoastiutlo()
        Cadastrocurso.pessoas_cadastradas()

    elif opcao == 2:
        Cadastrocurso.cadastrotitulo()
        while True:
            nome = input('Nome: ').strip()
            if nome:
                break
            else:
                print('\033[31mErro! O nome não pode estar vazio.\033[m')
        while True:
            try:
                idade = int(input('Idade: '))
                if idade >= 0:
                    break
                else:
                    print('\033[31mErro! Digite uma idade válida.\033[m')
            except ValueError:
                print('\033[31mErro! Digite uma idade válida.\033[m')

        Cadastrocurso.cadastro(nome, idade)

    elif opcao == 3:
        Cadastrocurso.apagar_pessoa()
    else:
        print('\033[31mErro! Opção inválida.\033[m')