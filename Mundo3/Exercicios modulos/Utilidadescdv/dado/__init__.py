def leiadinheiro(p):
    valido=False
    while not valido:
        entrada=str(input(p)).replace(',','.').strip()
        if entrada.isalpha():
            print(f'ERROR: "{entrada}" e um preço invalido!')
        else:
            valido=True
            return float(entrada)