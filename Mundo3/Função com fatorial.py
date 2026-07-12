def fatorial(n, show=True):
    f = 1
    for c in range(n,0,-1):
        f *= c
        if show:
            if c>1:
                print(c,end=' x ')
            else:
                print(c,end=' = ')
    return f


print(fatorial(5,True))
print(fatorial(5,False))