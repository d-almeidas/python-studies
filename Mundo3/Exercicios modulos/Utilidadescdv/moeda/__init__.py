
def metade(num, formato=False):
    res=num/2
    return moeda(res) if formato else res

def dobro(num, formato=False):
    res= num*2
    return moeda(res) if formato else res

def aumentar(p,porcentagem=0, formato=False):
    porcent=(porcentagem/100)+1
    aum=p*porcent
    res=aum
    return moeda(res) if formato else res

def diminuir(p,porcentagem=0,formato=False):
    porcent=(porcentagem/100)-1
    positivo=porcent*-1
    dimin=p*positivo
    res=dimin
    return moeda(res) if formato else res

def moeda(p):
    return f'R${p:.2f}'

def resumo(p,aumt=0,dimin=0):
    print('-'*30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-'*30)
    print(f'Preço analisado: \t{moeda(p)}')
    print(f'Dobro do preço: \t{moeda(dobro(p))}')
    print(f'Metade do preço: \t{moeda(metade(p))}')
    print(f'Aumento de {aumt}% :\t{moeda(aumentar(p,aumt))}')
    print(f'Diminuição de {dimin}% :\t{moeda(diminuir(p,dimin))}')
    print('-'*30)