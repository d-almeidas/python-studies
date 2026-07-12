def notas(*n, sit=False):
    dicionario = {}
    dicionario['total'] = len(n)
    dicionario['maior'] = max(n)
    dicionario['menor'] = min(n)
    dicionario['media'] = sum(n)/len(n)
    if sit==True:
        if dicionario['media'] >= 7:
            dicionario['Situação:']='boa'
        elif dicionario['media'] >= 5:
            dicionario['Situação:']='ok'
        else:
            dicionario['Situação:']='ruim'
    return dicionario

resp= notas(5.5,2.5,1.5,sit=True)
print(resp)

